# ADR-002: Deterministic Local Embedding Baseline

- Status: Accepted
- Date: 2026-09-01

## Context

The first retrieval milestone needs to run without an API key, model download, GPU, or external
embedding provider. It must still exercise vector indexing, tenant filters, ranking, citations, and
evaluation in Qdrant.

## Decision

Use a 128-dimension feature-hashing vector as the first local baseline. Words are hashed into vector
positions and the result is normalized before cosine search. Keep the embedding implementation behind
one function so a hosted or local semantic model can replace it later.

## Consequences

- The demo is deterministic, free, fast, and easy to test.
- It proves the retrieval plumbing, not semantic language understanding.
- Hash collisions and vocabulary mismatch reduce retrieval quality on realistic datasets.
- Future embedding comparisons can use this implementation as a measurable baseline.

## Alternatives

- Hosted embeddings offer stronger semantics but require credentials and create variable cost.
- A local transformer offers stronger semantics but adds a large model download and slower setup.
- TF-IDF is equally explainable but does not map as directly to the planned vector-service boundary.
