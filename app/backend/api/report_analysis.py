from fastapi import APIRouter, UploadFile, File
import shutil

from app.multimodal.ocr import OCRProcessor
from app.multimodal.report_analyzer import ReportAnalyzer

router = APIRouter()

@router.post("/analyze-report")
async def analyze_report(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    ocr = OCRProcessor()

    text = ocr.extract_text(
        file_path
    )

    analyzer = ReportAnalyzer()

    result = analyzer.analyze(
        text
    )

    return {
        "ocr_text": text,
        "analysis": result
    }