from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Agent 777 Gateway Service",
    description="API Gateway for the Agent 777 Security Operations Platform",
    version="1.0.0",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Agent 777 Gateway Service 🚀"
    }