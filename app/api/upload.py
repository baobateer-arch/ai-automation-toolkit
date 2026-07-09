from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import uuid

from app.services.pdf_service import PDFService
from app.services.document_ai_service import DocumentAIService
from app.database import async_session
from app.models.report import Report
from app.services.report_export_service import generate_pdf, generate_docx

router = APIRouter()

UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {".pdf"}


async def _save_and_extract(file: UploadFile) -> tuple[str, str]:
    ext = os.path.splitext(file.filename)[1].lower()
    safe_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, safe_name)
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    text = PDFService.extract_text(file_path)
    return text, file.filename


@router.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    text, original_filename = await _save_and_extract(file)
    return {
        "filename": original_filename,
        "text_length": len(text),
        "preview": text[:500],
    }


@router.post("/api/analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    text, original_filename = await _save_and_extract(file)

    if not text.strip():
        raise HTTPException(status_code=400, detail="No extractable text found in PDF")

    result = await DocumentAIService.analyze(text)

    # Save to database
    async with async_session() as session:
        report = Report(
            filename=original_filename,
            summary=result.get("summary", ""),
            key_points=result.get("key_points", []),
            risks=result.get("risks", []),
            suggestions=result.get("suggestions", []),
        )
        session.add(report)
        await session.commit()
        await session.refresh(report)
        result["id"] = report.id
        result["filename"] = report.filename
        result["created_at"] = report.created_at.isoformat()

    return result


@router.get("/api/reports")
async def list_reports():
    async with async_session() as session:
        from sqlalchemy import select, desc
        stmt = select(Report).order_by(desc(Report.created_at)).limit(50)
        reports = (await session.execute(stmt)).scalars().all()
        return [
            {
                "id": r.id,
                "filename": r.filename,
                "summary": (r.summary[:100] + "...") if len(r.summary) > 100 else r.summary,
                "created_at": r.created_at.isoformat(),
            }
            for r in reports
        ]


@router.get("/api/reports/{report_id}")
async def get_report(report_id: int):
    async with async_session() as session:
        from sqlalchemy import select
        stmt = select(Report).where(Report.id == report_id)
        report = (await session.execute(stmt)).scalar_one_or_none()
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        return {
            "id": report.id,
            "filename": report.filename,
            "summary": report.summary,
            "key_points": report.key_points,
            "risks": report.risks,
            "suggestions": report.suggestions,
            "created_at": report.created_at.isoformat(),
        }


@router.get("/api/reports/{report_id}/export/pdf")
async def export_report_pdf(report_id: int):
    async with async_session() as session:
        from sqlalchemy import select
        stmt = select(Report).where(Report.id == report_id)
        report = (await session.execute(stmt)).scalar_one_or_none()
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        filepath = generate_pdf(report)
        return FileResponse(filepath, media_type="application/pdf", filename=f"report_{report.id}.pdf")


@router.get("/api/reports/{report_id}/export/docx")
async def export_report_docx(report_id: int):
    async with async_session() as session:
        from sqlalchemy import select
        stmt = select(Report).where(Report.id == report_id)
        report = (await session.execute(stmt)).scalar_one_or_none()
        if not report:
            raise HTTPException(status_code=404, detail="Report not found")
        filepath = generate_docx(report)
        return FileResponse(
            filepath,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=f"report_{report.id}.docx",
        )
