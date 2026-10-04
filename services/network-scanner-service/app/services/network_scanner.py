import socket

from shared.schemas.scan import PortResult


class NetworkScanner:

    def scan(
        self,
        target: str,
        ports: list[int],
        timeout: float,
    ) -> list[PortResult]:

        results = []

        for port in ports:
            state = self._check_port(
                target=target,
                port=port,
                timeout=timeout,
            )

            service = self._identify_service(port) if state == "open" else None

            results.append(
                PortResult(
                    port=port,
                    state=state,
                    service=service,
                )
            )

        return results

    @staticmethod
    def _check_port(
        target: str,
        port: int,
        timeout: float,
    ) -> str:

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)

                result = sock.connect_ex((target, port))

                if result == 0:
                    return "open"

                return "closed"

        except socket.timeout:
            return "timeout"

        except socket.gaierror:
            return "unreachable"

        except OSError:
            return "unreachable"

    @staticmethod
    def _identify_service(port: int) -> str | None:

        common_services = {
            21: "ftp",
            22: "ssh",
            23: "telnet",
            25: "smtp",
            53: "dns",
            80: "http",
            110: "pop3",
            143: "imap",
            443: "https",
            3306: "mysql",
            5432: "postgresql",
            6379: "redis",
            8080: "http-alt",
        }

        return common_services.get(port)