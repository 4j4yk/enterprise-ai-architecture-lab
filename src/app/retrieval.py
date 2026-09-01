"""Qdrant storage and tenant-filtered search."""

from uuid import NAMESPACE_URL, uuid5

from qdrant_client import QdrantClient, models

from app.embedding import VECTOR_SIZE, embed
from app.models import Document, SearchResult

COLLECTION_NAME = "enterprise_documents"
INDEX_VERSION = "local-hash-v1"


class RetrievalService:
    def __init__(self, client: QdrantClient) -> None:
        self.client = client

    def ensure_collection(self) -> None:
        if not self.client.collection_exists(COLLECTION_NAME):
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(
                    size=VECTOR_SIZE,
                    distance=models.Distance.COSINE,
                ),
            )

    def index(self, documents: list[Document]) -> int:
        self.ensure_collection()
        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                models.PointStruct(
                    id=str(uuid5(NAMESPACE_URL, document.id)),
                    vector=embed(f"{document.title} {document.text}"),
                    payload=document.model_dump(),
                )
                for document in documents
            ],
        )
        return len(documents)

    def search(self, tenant_id: str, query: str, limit: int = 5) -> list[SearchResult]:
        self.ensure_collection()
        response = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=embed(query),
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="tenant_id",
                        match=models.MatchValue(value=tenant_id),
                    )
                ]
            ),
            limit=limit,
            with_payload=True,
        )

        results = []
        for point in response.points:
            payload = point.payload or {}
            results.append(
                SearchResult(
                    document_id=str(payload["id"]),
                    title=str(payload["title"]),
                    text=str(payload["text"]),
                    source_uri=str(payload["source_uri"]),
                    score=round(point.score, 4),
                )
            )
        return results
