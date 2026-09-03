import pytest

from app.ingestion import chunk_document, document_from_html, document_from_markdown


def test_markdown_adapter_keeps_text_and_source_metadata() -> None:
    document = document_from_markdown(
        document_id="guide",
        tenant_id="tenant-a",
        title="Guide",
        markdown="# Setup\nRead the [install guide](https://example.com/install).",
        source_uri="https://example.com/guide",
    )

    assert document.text == "Setup Read the install guide."
    assert document.content_type == "markdown"
    assert document.source_uri == "https://example.com/guide"


def test_html_adapter_extracts_visible_text() -> None:
    document = document_from_html(
        document_id="page",
        tenant_id="tenant-a",
        title="Page",
        html="<main><h1>Delivery</h1><p>Ships in two days.</p></main>",
        source_uri="https://example.com/page",
    )

    assert document.text == "Delivery Ships in two days."
    assert document.content_type == "html"


def test_chunking_preserves_tenant_and_citation_metadata() -> None:
    document = document_from_markdown(
        document_id="guide",
        tenant_id="tenant-a",
        title="Guide",
        markdown="one two three four five six seven",
        source_uri="https://example.com/guide",
    )

    chunks = chunk_document(document, size=4, overlap=1)

    assert [chunk.text for chunk in chunks] == ["one two three four", "four five six seven"]
    assert chunks[1].parent_id == "guide"
    assert chunks[1].chunk_index == 1
    assert chunks[1].tenant_id == "tenant-a"
    assert chunks[1].source_uri == "https://example.com/guide"


@pytest.mark.parametrize("size, overlap", [(0, 0), (4, -1), (4, 4)])
def test_chunking_rejects_invalid_settings(size: int, overlap: int) -> None:
    document = document_from_markdown(
        document_id="guide",
        tenant_id="tenant-a",
        title="Guide",
        markdown="some text",
        source_uri="https://example.com/guide",
    )

    with pytest.raises(ValueError):
        chunk_document(document, size=size, overlap=overlap)
