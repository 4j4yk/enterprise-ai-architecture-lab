"""A small deterministic embedding for a reproducible local demo."""

import hashlib
import math
import re

VECTOR_SIZE = 128


def embed(text: str) -> list[float]:
    """Hash words into a fixed-size normalized vector."""
    vector = [0.0] * VECTOR_SIZE
    for word in re.findall(r"[a-z0-9]+", text.lower()):
        digest = hashlib.sha256(word.encode()).digest()
        position = int.from_bytes(digest[:4]) % VECTOR_SIZE
        vector[position] += 1.0

    length = math.sqrt(sum(value * value for value in vector))
    return [value / length for value in vector] if length else vector
