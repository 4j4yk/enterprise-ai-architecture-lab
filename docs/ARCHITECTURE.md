# Target Architecture

## Logical flow

```text
Public AEM pages + synthetic catalog + documents
                     |
              ingestion workers
                     |
      normalization, chunking, metadata
                     |
       embeddings + sparse representation
                     |
                  Qdrant
                     |
          gRPC retrieval service
                     |
        LangGraph orchestration layer
          |          |           |
       search     classifier   safe tools
          |          |           |
           human approval gateway
                     |
              FastAPI application
                     |
        demo UI / REST / GraphQL adapter

Cross-cutting: MLflow evaluation, OpenTelemetry, security, CI/CD
```

## Service boundaries

- `api`: public REST API, authentication hooks, validation, rate limits, request correlation.
- `orchestrator`: LangGraph state, routing, tools, approval interrupts, fallback behavior.
- `retrieval`: gRPC contract for search, hybrid retrieval, reranking, citations, and diagnostics.
- `ingestion`: source adapters, normalization, chunking experiments, embedding jobs, index versioning.
- `evaluation`: datasets, retrieval metrics, response scorers, classical-ML benchmark, regression gates.
- `observability`: OpenTelemetry traces/metrics and MLflow GenAI traces.

## Initial technology choices

- Python 3.12
- FastAPI and Pydantic
- LangGraph
- Qdrant
- PostgreSQL
- Redis optional after measurement
- gRPC and Protocol Buffers
- MLflow
- OpenTelemetry
- scikit-learn
- Docker Compose locally
- Kubernetes and Terraform after local behavior is stable

## Nonfunctional requirements

- Tenant isolation by metadata filters, tested explicitly.
- Citations on grounded responses.
- Safe fallback when retrieval or model providers fail.
- Idempotent ingestion and tool operations.
- Prompt and index version traceability.
- No secrets or sensitive content in logs.
- Measurable latency, retrieval quality, token use, and error rates.
- Human approval for any simulated state-changing action.
