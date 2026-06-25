from fastapi import FastAPI

from app.backend.api.health import router as health_router
from app.backend.api.upload import router as upload_router
from app.backend.api.retrieve import router as retrieve_router
from app.backend.api.chat import router as chat_router
from app.backend.api.multimodal import router as multimodal_router
from app.backend.api.report_analysis import router as report_router


app = FastAPI(
    title="MediAssist AI",
    version="1.0"
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(retrieve_router)
app.include_router(chat_router)
app.include_router(multimodal_router)
app.include_router(report_router)


@app.get("/")
def home():
    return {
        "message": "MediAssist AI Running Successfully"
    }