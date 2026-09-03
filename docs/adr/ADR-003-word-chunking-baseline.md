# ADR-003: Word-Based Chunking Baseline

- Status: Accepted
- Date: 2026-09-03

## Context

Long pages and documents must be split before retrieval. The first implementation needs predictable
behavior that can be tested without a tokenizer tied to one model provider.

## Decision

Start with word-count chunks and configurable overlap. Every chunk keeps the parent document ID,
tenant, title, source URL, access label, version, and a zero-based chunk index.

## Consequences

- Chunk boundaries and tests are easy to understand and reproduce.
- Overlap reduces the chance of losing context at a boundary but increases index size.
- Word counts do not match model token counts and may split sentences.
- Later experiments can compare token-aware and semantic chunking against this baseline.

## Alternatives

- Model-token chunking controls prompt size more precisely but couples ingestion to a tokenizer.
- Sentence or semantic chunking can preserve meaning better but adds libraries and more tuning.
- Indexing whole documents is simpler but performs poorly for longer mixed-topic content.
