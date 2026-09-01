from app.catalog import catalog_documents


def test_catalog_adapter_creates_normalized_documents() -> None:
    documents = catalog_documents("tenant-a")

    assert len(documents) == 3
    assert all(document.tenant_id == "tenant-a" for document in documents)
    assert all(document.source_uri.startswith("https://") for document in documents)
    assert documents[0].content_type == "product"
