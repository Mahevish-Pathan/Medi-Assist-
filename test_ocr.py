from app.multimodal.ocr import OCRProcessor

ocr = OCRProcessor()

text = ocr.extract_text(
    r"uploads\Screenshot 2026-06-24 231046.png"
)

print(text)