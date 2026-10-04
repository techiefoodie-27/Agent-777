from pydantic import BaseModel, Field, field_validator


class ScanRequest(BaseModel):
    target: str = Field(
        ...,
        description="IP address or hostname to scan",
        examples=["127.0.0.1"],
    )

    ports: list[int] = Field(
        default=[22, 80, 443],
        description="TCP ports to scan",
        examples=[[22, 80, 443]],
    )

    timeout: float = Field(
        default=1.0,
        gt=0,
        le=10,
        description="Connection timeout in seconds",
    )

    @field_validator("ports")
    @classmethod
    def validate_ports(cls, ports: list[int]) -> list[int]:
        if not ports:
            raise ValueError("At least one port must be provided")

        if len(ports) > 100:
            raise ValueError("A maximum of 100 ports can be scanned at once")

        if any(port < 1 or port > 65535 for port in ports):
            raise ValueError("Ports must be between 1 and 65535")

        return sorted(set(ports))


class PortResult(BaseModel):
    port: int
    state: str
    service: str | None = None


class ScanResponse(BaseModel):
    target: str
    ports_scanned: int
    open_ports: int
    results: list[PortResult]