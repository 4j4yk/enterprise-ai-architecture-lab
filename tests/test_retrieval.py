from qdrant_client import QdrantClient

from app.catalog import catalog_documents
from app.retrieval import RetrievalService


def test_search_returns_relevant_product_and_citation() -> None:
    service = RetrievalService(QdrantClient(":memory:"))
    service.index(catalog_documents("tenant-a"))

    results = service.search("tenant-a", "portable laptop for a developer", limit=2)

    assert results[0].title == "Pro 14 Laptop"
    assert results[0].source_uri.startswith("https://")


def test_search_does_not_cross_tenant_boundary() -> None:
    service = RetrievalService(QdrantClient(":memory:"))
    service.index(catalog_documents("tenant-a"))

    assert service.search("tenant-b", "laptop") == []
