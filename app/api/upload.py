from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid

from app.services.pdf_service import PDFService
from app.services.document_ai_service import DocumentAIService

router = APIRouter()

UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {".pdf"}


@router.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # 閬垮厤鏂囦欢鍚嶅啿绐?
    safe_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, safe_name)

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    try:
        text = PDFService.extract_text(file_path)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to extract text from PDF")

    return {
        "filename": file.filename,
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

    safe_name = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, safe_name)

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    try:
        text = PDFService.extract_text(file_path)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to extract text from PDF")

    if not text.strip():
        raise HTTPException(status_code=400, detail="No extractable text found in PDF")

    try:
        result = await DocumentAIService.analyze(text)
    except Exception:
        raise HTTPException(status_code=500, detail="AI analysis failed")

    return result
