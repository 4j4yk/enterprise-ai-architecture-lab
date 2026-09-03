"""Small retrieval evaluation that runs without external services."""

from dataclasses import dataclass

from qdrant_client import QdrantClient

from app.catalog import catalog_documents
from app.retrieval import RetrievalService
from app.sample_content import sample_documents


@dataclass(frozen=True)
class EvaluationCase:
    query: str
    expected_document_id: str


CASES = [
    EvaluationCase("developer laptop with memory", "product-laptop-pro-14"),
    EvaluationCase("color accurate 4k display", "product-monitor-4k-27"),
    EvaluationCase("noise cancellation meeting microphone", "product-headset-nc-1"),
    EvaluationCase("how many days do I have to return an unused item", "policy-returns-chunk-0"),
    EvaluationCase("free shipping order amount", "policy-shipping-chunk-0"),
]


def evaluate_recall_at_one() -> float:
    service = RetrievalService(QdrantClient(":memory:"))
    service.index(catalog_documents() + sample_documents())
    correct = sum(
        service.search("demo-store", case.query, limit=1)[0].document_id
        == case.expected_document_id
        for case in CASES
    )
    return correct / len(CASES)


if __name__ == "__main__":
    print(f"Recall@1: {evaluate_recall_at_one():.2f} ({len(CASES)} synthetic queries)")
