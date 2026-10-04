from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.scanner import router as scanner_router
from app.core.config import settings


api_router = APIRouter(
    prefix=settings.API_V1_PREFIX
)

api_router.include_router(health_router)
api_router.include_router(scanner_router)