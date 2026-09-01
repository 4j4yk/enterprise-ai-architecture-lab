# Implementation Roadmap

## Milestone 0 - Foundation

Status: Complete locally on 2026-09-01. CI workflow is configured but awaits its first GitHub run.

- Runnable FastAPI health service
- Docker Compose for PostgreSQL, Qdrant, and MLflow
- Dependency lock, tests, linting, and CI
- Configuration and secret-handling conventions
- ADR-001 for the initial architecture

## Milestone 1 - Ingestion and retrieval

Status: In progress. Synthetic catalog normalization, Qdrant vector search, tenant filtering,
citations, and a three-query baseline evaluation are complete.

- Public AEM content adapter
- Synthetic Mage-OS catalog adapter
- PDF/Markdown/text adapter
- Normalized document schema
- Chunk-size and overlap experiments
- Qdrant dense, sparse, and hybrid retrieval
- Tenant filtering and citation metadata
- Recall@k, MRR/nDCG, latency, and index-cost report

## Milestone 2 - Agentic workflow

- LangGraph routing and tool nodes
- Persistent checkpoints
- Human approval interrupts
- Context and memory policy
- Model routing and retrieval-only fallback
- Failure injection and recovery tests

## Milestone 3 - Distributed contracts

- Retrieval `.proto` contract
- Python gRPC client/server
- Versioning and compatibility tests
- Deadlines, retries, health checks, and correlation IDs
- REST-to-gRPC trace propagation

## Milestone 4 - Evaluation and observability

- MLflow prompt registry and evaluation dataset
- Groundedness, relevance, safety, and task scorers
- OpenTelemetry traces and metrics
- Latency, token, error, and cost dashboards
- Regression gates in CI

## Milestone 5 - Classical ML benchmark

- Synthetic commerce/support ticket dataset
- TF-IDF + logistic regression baseline
- Embedding classifier
- LLM zero/few-shot classifier
- Accuracy, precision, recall, F1, latency, cost, and abstention comparison
- Drift simulation and monitoring

## Milestone 6 - Cloud-native delivery

- Production Dockerfiles
- Kubernetes manifests or Helm
- Terraform modules
- Security scanning and SBOM
- Load tests, resilience tests, resource and cost analysis

## Milestone 7 - Snowflake proof of concept

- Synthetic data ingestion
- Governed schemas and transformations
- Data-quality checks
- RAG integration option
- Access, masking, performance, and cost tradeoff report

## Milestone 8 - Portfolio release

- Live demo
- Architecture and sequence diagrams
- Threat model
- At least five ADRs
- Evaluation and load-test reports
- Demo script and interview walkthrough
- Evidence-backed resume bullets
