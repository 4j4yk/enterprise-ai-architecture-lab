from fastapi import FastAPI, Response, status
from qdrant_client import QdrantClient

from app.catalog import catalog_documents
from app.config import Settings
from app.dependencies import check_dependencies
from app.models import SearchRequest, SearchResponse
from app.retrieval import INDEX_VERSION, RetrievalService
from app.sample_content import sample_documents

app = FastAPI(title="Enterprise AI Architecture Lab", version="0.1.0")


def retrieval_service() -> RetrievalService:
    settings = Settings.from_environment()
    return RetrievalService(QdrantClient(url=settings.qdrant_url))


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness check: the API process is running."""
    return {"status": "ok"}


@app.get("/ready")
def readiness(response: Response) -> dict[str, object]:
    """Readiness check: services used by the API are reachable."""
    checks = check_dependencies(Settings.from_environment())
    ready = all(checks.values())

    if not ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return {
        "status": "ready" if ready else "not_ready",
        "dependencies": checks,
    }


@app.post("/demo/seed")
def seed_demo_catalog() -> dict[str, object]:
    documents = catalog_documents() + sample_documents()
    indexed = retrieval_service().index(documents)
    return {"indexed": indexed, "tenant_id": "demo-store", "index_version": INDEX_VERSION}


@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    results = retrieval_service().search(request.tenant_id, request.query, request.limit)
    return SearchResponse(results=results, index_version=INDEX_VERSION)
