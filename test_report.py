from app.multimodal.ocr import OCRProcessor
from app.multimodal.report_analyzer import ReportAnalyzer

ocr = OCRProcessor()

text = ocr.extract_text(
    r"uploads\Screenshot 2026-06-24 231046.png"
)

analyzer = ReportAnalyzer()

result = analyzer.analyze(text)

print(result)