from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil
import os

from app.backend.services.ingestion_service import (
    IngestionService
)

router = APIRouter()

# Create upload directory safely
UPLOAD_DIR = os.path.join(
    "data",
    "raw_data"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

ingestion_service = IngestionService()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    # Save uploaded file
    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Process PDF/Image
    total_chunks = (
        ingestion_service.ingest_document(
            file_path
        )
    )

    return {
        "message": "Document processed successfully",
        "filename": file.filename,
        "chunks": total_chunks
    }