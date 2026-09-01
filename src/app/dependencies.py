"""Small network checks used by the readiness endpoint."""

import socket
from urllib.error import URLError
from urllib.request import urlopen

from app.config import Settings


def check_tcp(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def check_http(url: str, timeout: float = 1.0) -> bool:
    try:
        with urlopen(url, timeout=timeout) as response:
            return response.status < 500
    except (OSError, URLError):
        return False


def check_dependencies(settings: Settings) -> dict[str, bool]:
    return {
        "postgres": check_tcp(settings.postgres_host, settings.postgres_port),
        "qdrant": check_http(f"{settings.qdrant_url.rstrip('/')}/healthz"),
        "mlflow": check_http(f"{settings.mlflow_url.rstrip('/')}/health"),
    }
