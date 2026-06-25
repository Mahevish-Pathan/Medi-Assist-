from PIL import Image
import pytesseract
from langchain_core.documents import Document
import os


class ImageLoader:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    def load_image(self, image_path):

        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        image = Image.open(image_path)

        extracted_text = pytesseract.image_to_string(
            image
        )

        document = Document(
            page_content=extracted_text,
            metadata={
                "source": image_path
            }
        )

        return [document]