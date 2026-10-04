from fastapi import APIRouter


router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "service": "network-scanner-service",
        "version": "1.0.0",
    }