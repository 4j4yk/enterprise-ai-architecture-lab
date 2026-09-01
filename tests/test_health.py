from fastapi.testclient import TestClient
from pytest import MonkeyPatch

from app.main import app


def test_health() -> None:
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_when_dependencies_are_available(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.check_dependencies",
        lambda _settings: {"postgres": True, "qdrant": True, "mlflow": True},
    )

    response = TestClient(app).get("/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_not_ready_when_a_dependency_is_unavailable(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.check_dependencies",
        lambda _settings: {"postgres": True, "qdrant": False, "mlflow": True},
    )

    response = TestClient(app).get("/ready")

    assert response.status_code == 503
    assert response.json() == {
        "status": "not_ready",
        "dependencies": {"postgres": True, "qdrant": False, "mlflow": True},
    }
