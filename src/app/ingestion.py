"""Adapters and chunking shared by document ingestion sources."""

import re
from html.parser import HTMLParser

from app.models import Document


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def _clean_whitespace(text: str) -> str:
    return " ".join(text.split())


def document_from_markdown(
    *, document_id: str, tenant_id: str, title: str, markdown: str, source_uri: str
) -> Document:
    """Convert simple Markdown content into the common document model."""
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", markdown)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[`#>*_~-]", " ", text)
    return Document(
        id=document_id,
        tenant_id=tenant_id,
        title=title,
        text=_clean_whitespace(text),
        source_uri=source_uri,
        content_type="markdown",
    )


def document_from_html(
    *, document_id: str, tenant_id: str, title: str, html: str, source_uri: str
) -> Document:
    """Convert already-fetched public HTML into the common document model."""
    parser = _TextExtractor()
    parser.feed(html)
    return Document(
        id=document_id,
        tenant_id=tenant_id,
        title=title,
        text=_clean_whitespace(" ".join(parser.parts)),
        source_uri=source_uri,
        content_type="html",
    )


def chunk_document(document: Document, size: int = 80, overlap: int = 15) -> list[Document]:
    """Split a document by words while retaining citation and tenant metadata."""
    if size < 1:
        raise ValueError("size must be at least 1")
    if overlap < 0 or overlap >= size:
        raise ValueError("overlap must be between 0 and size - 1")

    words = document.text.split()
    if not words:
        return []

    chunks = []
    step = size - overlap
    for index, start in enumerate(range(0, len(words), step)):
        chunk_words = words[start : start + size]
        chunks.append(
            document.model_copy(
                update={
                    "id": f"{document.id}-chunk-{index}",
                    "text": " ".join(chunk_words),
                    "parent_id": document.id,
                    "chunk_index": index,
                }
            )
        )
        if start + size >= len(words):
            break
    return chunks
