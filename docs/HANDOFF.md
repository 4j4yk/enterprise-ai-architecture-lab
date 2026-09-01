# Agent Handoff

## Objective

Build a portfolio-quality enterprise AI system that closes these evidence gaps:

- Hands-on gRPC implementation
- Named vector database implementation
- Measured RAG retrieval quality
- Classical ML versus LLM tradeoff analysis
- MLflow prompt/evaluation lifecycle
- OpenTelemetry AI observability
- Snowflake integration proof of concept
- Quantified latency, quality, reliability, and cost results

## Candidate context

The owner is an experienced Solution Architect and Technical Lead with verified experience in Python, Java/J2EE, REST/GraphQL/SOAP APIs, event-driven systems, AWS/Azure, Docker, Kubernetes patterns, CI/CD, SQL, RAG, embeddings, vector retrieval concepts, agentic workflows, evaluation, guardrails, Adobe Commerce, AEM, CRM-connected processes, MES/Tulip workflows, and operations digitization.

Existing public demonstrations that may be integrated only through public interfaces or exported synthetic data:

- AEM demo: `https://aem-demo.ajayk.xyz/`
- AEM source: `https://github.com/4j4yk/aem-demo`
- Mage-OS demo: `https://store.ajayk.xyz/`
- GitHub profile: `https://github.com/4j4yk`

Do not copy secrets or private data from those projects.

## Target system

Create an enterprise content-and-commerce AI assistant that:

1. Ingests public AEM pages, synthetic Mage-OS catalog data, and sample documents.
2. Creates normalized documents with source, tenant, content type, access label, and version metadata.
3. Evaluates multiple chunk sizes and overlaps.
4. Stores dense and sparse representations in Qdrant.
5. Supports semantic, lexical, and hybrid retrieval plus reranking.
6. Uses LangGraph for durable, stateful tool workflows.
7. Requires approval before simulated write actions.
8. Exposes REST/GraphQL-facing APIs and an internal gRPC retrieval service.
9. Uses MLflow for prompt versions, traces, evaluation datasets, and comparisons.
10. Uses OpenTelemetry for application traces and metrics.
11. Compares classical ML, embedding-based, and LLM ticket classification.
12. Optionally demonstrates Snowflake ingestion/modeling and retrieval integration.

## Immediate next task

Continue Milestone 1 with public content and chunking:

- Add a public-page or Markdown adapter.
- Add chunk size and overlap experiments.
- Compare the local hash baseline with a real embedding model.
- Expand the evaluation dataset before claiming retrieval quality.

## Handoff update format

At the end of each work session, append:

```text
Date:
Completed:
Verified by:
Files changed:
Decisions/ADRs:
Known issues:
Next exact task:
Resume evidence unlocked:
```

If no resume evidence was unlocked, write `None`.

## Work sessions

Date: 2026-09-01
Completed: Milestone 0 local foundation; locked dependencies; added dependency readiness checks and CI configuration; corrected the MLflow host port to avoid the macOS port 5000 conflict.
Verified by: 3 passing tests, Ruff, mypy, Docker Compose validation, and live checks against PostgreSQL, Qdrant, and MLflow.
Files changed: API configuration and readiness modules, tests, Makefile, Compose, environment example, CI workflow, lockfile, README, roadmap, evidence ledger, and ADR-001.
Decisions/ADRs: ADR-001 accepted. MLflow is exposed on host port 5050 while retaining container port 5000.
Known issues: GitHub Actions has not run remotely yet. No ingestion or retrieval behavior exists.
Next exact task: Define and test the normalized document model plus a synthetic catalog adapter.
Resume evidence unlocked: A local, tested FastAPI foundation with containerized dependencies and explicit readiness behavior; no RAG claim yet.

Date: 2026-09-01
Completed: Added normalized documents, a synthetic catalog adapter, deterministic local embeddings,
Qdrant indexing and tenant-filtered search, citation-bearing API responses, a retrieval evaluation,
and ADR-002.
Verified by: 7 passing tests, Ruff, mypy, Recall@1 of 1.00 on 3 synthetic queries, and a live
FastAPI-to-Qdrant seed/search run.
Files changed: Source models, catalog, embedding, retrieval, evaluation, API routes, tests, README,
roadmap, evidence ledger, Compose configuration, Makefile, and ADR-002.
Decisions/ADRs: ADR-002 accepted for a deterministic hash-embedding baseline with explicit limits.
Known issues: Evaluation dataset is intentionally tiny; hash embeddings do not prove semantic quality;
public-page ingestion, chunking experiments, hybrid search, reranking, and later milestones remain open.
Next exact task: Add a public Markdown/page adapter and chunking experiment with a larger judged dataset.
Resume evidence unlocked: Tenant-filtered Qdrant vector retrieval with citations and a reproducible
synthetic baseline; no production-scale or LLM-quality claim.
