import fitz  # PyMuPDF


class PDFService:

    @staticmethod
    def extract_text(file_path: str) -> str:
        doc = fitz.open(file_path)
        try:
            text = ""
            for page in doc:
                text += page.get_text()
            return text.strip()
        finally:
            doc.close()
