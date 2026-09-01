# ADR-001: Initial Platform Shape

- Status: Accepted
- Date: 2026-09-01

## Context

The project must demonstrate enterprise RAG, agentic orchestration, distributed APIs, evaluation, observability, and cloud-native delivery while remaining runnable on a developer workstation.

## Decision

Use Python/FastAPI for the public service, LangGraph for durable orchestration, Qdrant for vector and hybrid retrieval, PostgreSQL for relational and checkpoint data, gRPC for the internal retrieval boundary, MLflow for evaluation and prompt lifecycle, and OpenTelemetry for cross-service telemetry. Start with Docker Compose and add Kubernetes/Terraform only after behavior and measurements are stable.

## Consequences

- The stack directly exercises the target skills.
- Local development remains feasible.
- Multiple infrastructure services increase setup complexity.
- gRPC must represent a real service boundary rather than decorative technology.
- Snowflake remains a later optional integration to avoid blocking the core system.

## Alternatives

- PostgreSQL/pgvector: simpler operational footprint, but less direct evidence of a dedicated vector database and hybrid-search architecture.
- Fully managed cloud stack: closer to production, but introduces cost and account dependencies too early.
- Single-process monolith: faster initially, but insufficient for distributed-contract and trace-propagation evidence.
