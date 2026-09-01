# Enterprise AI Architecture Lab

An independent, hands-on reference implementation for enterprise AI architecture. The project grows
in small, measured milestones so every implemented claim has working code and tests behind it.

## Intended demonstrations

- Ingestion from AEM-style content, Mage-OS-style catalog data, and documents
- Preprocessing, chunking, embeddings, hybrid retrieval, reranking, and citations
- Tenant-aware Qdrant vector search
- Durable LangGraph workflows with human approval
- FastAPI REST endpoints and an internal gRPC boundary
- MLflow prompt versioning, evaluation, tracing, latency, and token-cost analysis
- OpenTelemetry traces and metrics
- Docker, Kubernetes, Terraform patterns, CI/CD, tests, and security scanning
- Classical ML versus embeddings versus LLM classification benchmark
- Optional Snowflake ingestion and retrieval proof of concept

## Current status

The foundation and first retrieval baseline run locally. Synthetic product records are normalized,
embedded with a deterministic local baseline, stored in Qdrant, and searched with tenant isolation
and source citations. Agent workflows and model-generated answers are not implemented yet.

## Architecture in one minute

```text
Synthetic catalog
      |
catalog adapter -> normalized Document objects
      |
local deterministic embedding -> Qdrant vector index
      |
tenant-filtered search -> ranked results + source URLs
      |
FastAPI /search endpoint
```

The code is intentionally separated by responsibility:

- `catalog.py` converts source-specific records into the common document model.
- `embedding.py` contains the replaceable embedding baseline.
- `retrieval.py` owns Qdrant indexing and search.
- `main.py` exposes the HTTP contract.
- `evaluation.py` measures the small retrieval dataset.

## Start here

Read [the handoff](docs/HANDOFF.md), then complete Milestone 0 in [the roadmap](docs/ROADMAP.md).

## Local setup

```bash
cp .env.example .env
make setup
docker compose up -d
make test
make run
```

The default health endpoint is `http://localhost:8000/health`.
The readiness endpoint is `http://localhost:8000/ready`, and MLflow is available at
`http://localhost:5050`.

## Try the retrieval flow

Seed the synthetic catalog:

```bash
curl -X POST http://localhost:8000/demo/seed
```

Search it:

```bash
curl -X POST http://localhost:8000/search \
  -H 'content-type: application/json' \
  -d '{"tenant_id":"demo-store","query":"portable developer laptop","limit":2}'
```

Run the reproducible baseline evaluation:

```bash
make evaluate
```

## Honest scope

- The catalog and evaluation set are synthetic and intentionally tiny.
- The local hash embedding is a plumbing baseline, not a production semantic model.
- No production scale, LLM answer quality, or cloud performance is claimed.
- Planned capabilities remain visible in [the roadmap](docs/ROADMAP.md).

## Safety

Use synthetic/public data only. Do not place employer, client, applicant, medical, financial, or other sensitive information in the repository.
