"""Synthetic catalog adapter used by the local demonstration."""

from app.models import Document

SYNTHETIC_PRODUCTS = [
    {
        "sku": "LAPTOP-PRO-14",
        "name": "Pro 14 Laptop",
        "description": "Portable developer laptop with 32 GB memory and a 12-hour battery.",
        "category": "Computers",
    },
    {
        "sku": "MONITOR-4K-27",
        "name": "27-inch 4K Monitor",
        "description": "Color-accurate 4K display with USB-C charging for office and design work.",
        "category": "Displays",
    },
    {
        "sku": "HEADSET-NC-1",
        "name": "Noise-Cancelling Headset",
        "description": "Wireless headset with active noise cancellation and a meeting microphone.",
        "category": "Audio",
    },
]


def catalog_documents(tenant_id: str = "demo-store") -> list[Document]:
    """Convert catalog records into the common document shape."""
    return [
        Document(
            id=f"product-{product['sku'].lower()}",
            tenant_id=tenant_id,
            title=product["name"],
            text=(
                f"{product['name']}. {product['description']} "
                f"Category: {product['category']}. SKU: {product['sku']}."
            ),
            source_uri=f"https://example.com/products/{product['sku'].lower()}",
            content_type="product",
        )
        for product in SYNTHETIC_PRODUCTS
    ]
