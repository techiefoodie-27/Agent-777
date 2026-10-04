from fastapi import APIRouter, HTTPException

from shared.schemas.scan import ScanRequest, ScanResponse
from app.services.scanner_client import ScannerClient


router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"],
)

scanner_client = ScannerClient()


@router.post("/scan", response_model=ScanResponse)
def scan_network(request: ScanRequest):

    try:
        return scanner_client.scan(
            target=request.target,
            ports=request.ports,
            timeout=request.timeout,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Network scanner service unavailable: {exc}",
        )