from fastapi import FastAPI

app = FastAPI(
    title="HablaAI",
    description="AI-powered Spanish learning application",
    version="0.1.0"
)

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
