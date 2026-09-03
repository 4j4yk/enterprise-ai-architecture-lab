"""Shared request and document models."""

from pydantic import BaseModel, Field


class Document(BaseModel):
    id: str
    tenant_id: str
    title: str
    text: str
    source_uri: str
    content_type: str = "text"
    access_label: str = "public"
    version: str = "1"
    parent_id: str | None = None
    chunk_index: int | None = None


class SearchRequest(BaseModel):
    tenant_id: str
    query: str = Field(min_length=2)
    limit: int = Field(default=5, ge=1, le=20)


class SearchResult(BaseModel):
    document_id: str
    title: str
    text: str
    source_uri: str
    score: float


class SearchResponse(BaseModel):
    results: list[SearchResult]
    index_version: str
