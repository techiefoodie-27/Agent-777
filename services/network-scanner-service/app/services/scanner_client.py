import httpx

from app.core.config import settings


class ScannerClient:

    def scan(
        self,
        target: str,
        ports: list[int],
        timeout: float,
    ) -> dict:

        payload = {
            "target": target,
            "ports": ports,
            "timeout": timeout,
        }

        response = httpx.post(
            f"{settings.NETWORK_SCANNER_URL}/scan",
            json=payload,
            timeout=timeout + 5,
        )

        response.raise_for_status()

        return response.json()