"""Small synthetic content samples used by the local demo."""

from app.ingestion import chunk_document, document_from_html, document_from_markdown
from app.models import Document


def sample_documents(tenant_id: str = "demo-store") -> list[Document]:
    returns = document_from_markdown(
        document_id="policy-returns",
        tenant_id=tenant_id,
        title="Returns and Exchanges",
        markdown="""
        # Returns and Exchanges

        Unused products can be returned within **30 days** of delivery. Keep the original packaging
        and order number. Refunds are sent to the original payment method after inspection.

        Opened headphones can only be returned when they are defective.
        """,
        source_uri="https://example.com/help/returns",
    )
    shipping = document_from_html(
        document_id="policy-shipping",
        tenant_id=tenant_id,
        title="Shipping Information",
        html="""
        <main><h1>Shipping</h1><p>Standard delivery takes three to five business days.</p>
        <p>Orders over $75 receive free standard shipping.</p></main>
        """,
        source_uri="https://example.com/help/shipping",
    )
    return chunk_document(returns, size=35, overlap=5) + chunk_document(
        shipping, size=35, overlap=5
    )
