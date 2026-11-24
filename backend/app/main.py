from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.spanish_tutor import get_tutor_response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="HablaAI",
    description="AI-powered Spanish learning application",
    version="0.2.0"
)

class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    conversation_id: str
    reply: str

@app.get("/")
def home():
    return {
        "message": "Welcome to HablaAI!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty.",
        )

    try:
        result = get_tutor_response(
            message=message,
            conversation_id=request.conversation_id,
        )
        return result

    except Exception:
        logger.exception("Gemini request failed")

        raise HTTPException(
            status_code=502,
            detail="The Spanish tutor could not get a response. Please try again.",
        )