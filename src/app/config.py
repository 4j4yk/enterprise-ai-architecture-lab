"""Application configuration loaded from environment variables."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    qdrant_url: str = "http://localhost:6333"
    mlflow_url: str = "http://localhost:5050"

    @classmethod
    def from_environment(cls) -> "Settings":
        return cls(
            postgres_host=os.getenv("POSTGRES_HOST", cls.postgres_host),
            postgres_port=int(os.getenv("POSTGRES_PORT", str(cls.postgres_port))),
            qdrant_url=os.getenv("QDRANT_URL", cls.qdrant_url),
            mlflow_url=os.getenv("MLFLOW_TRACKING_URI", cls.mlflow_url),
        )
