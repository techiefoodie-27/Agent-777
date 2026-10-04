from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.scanner import router as scanner_router


app = FastAPI(
    title="Agent 777 Network Scanner Service",
    description="Network scanning service for the Agent 777 Security Operations Platform",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(scanner_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Agent 777 Network Scanner Service 🚀"
    }
    