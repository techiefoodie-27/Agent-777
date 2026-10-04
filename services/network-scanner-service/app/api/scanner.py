from fastapi import APIRouter

from shared.schemas.scan import ScanRequest, ScanResponse
from app.services.network_scanner import NetworkScanner


router = APIRouter(
    prefix="/scan",
    tags=["Scanner"],
)

scanner = NetworkScanner()


@router.post("", response_model=ScanResponse)
def scan_network(request: ScanRequest):
    results = scanner.scan(
        target=request.target,
        ports=request.ports,
        timeout=request.timeout,
    )

    return ScanResponse(
        target=request.target,
        ports_scanned=len(request.ports),
        open_ports=sum(
            1 for result in results
            if result.state == "open"
        ),
        results=results,
    )