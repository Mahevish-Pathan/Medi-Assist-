from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-image")
async def upload_image(
    file: UploadFile = File(...)
):

    allowed_extensions = [
        ".png",
        ".jpg",
        ".jpeg"
    ]

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in allowed_extensions:

        return {
            "error":
            "Only png, jpg, jpeg allowed"
        }

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(
            await file.read()
        )

    return {
        "message": "Image uploaded successfully",
        "filename": file.filename
    }