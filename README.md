# Enterprise AI Architecture Lab

I created this project to work through the main parts of an enterprise AI system instead of only
describing them in architecture diagrams.

The first version covers a small retrieval flow. It takes synthetic product data, converts each
product into a common document format, creates a local vector representation, stores it in Qdrant,
and exposes search through FastAPI. Search results are filtered by tenant and include the source URL.

I am building the project in stages. The current code is deliberately small so I can test each part
before adding model APIs, agent workflows, or cloud infrastructure.

## What works today

- FastAPI health and readiness endpoints
- A synthetic product catalog adapter
- A shared document model with tenant and source metadata
- Deterministic local embeddings for the initial baseline
- Qdrant indexing and tenant-filtered vector search
- Source URLs in search results
- A small retrieval evaluation
- Automated tests, linting, type checks, and GitHub Actions
- Local PostgreSQL, Qdrant, and MLflow services through Docker Compose

The local embedding is based on feature hashing. I chose it for the first version because it is fast,
repeatable, and does not require an API key. It is useful for testing the retrieval design, but it is
not a replacement for a semantic embedding model. The reasoning and tradeoffs are recorded in
[ADR-002](docs/adr/ADR-002-local-embedding-baseline.md).

## How the current flow works

```text
synthetic products
       |
catalog adapter
       |
normalized documents
       |
local embeddings
       |
Qdrant
       |
FastAPI search endpoint
```

The main files are:

- `src/app/catalog.py` - converts product records into documents
- `src/app/models.py` - defines the API and document models
- `src/app/embedding.py` - creates the local vectors
- `src/app/retrieval.py` - indexes and searches Qdrant
- `src/app/main.py` - defines the API endpoints
- `src/app/evaluation.py` - runs the small retrieval check

## Run it locally

You need Python 3.12 or newer, [uv](https://docs.astral.sh/uv/), Docker, and Docker Compose.

```bash
cp .env.example .env
make setup
docker compose up -d
make test
make run
```

The API starts at `http://localhost:8000`. Useful endpoints are:

- `GET /health` - confirms the API process is running
- `GET /ready` - checks PostgreSQL, Qdrant, and MLflow
- `POST /demo/seed` - loads the three synthetic products into Qdrant
- `POST /search` - searches documents for one tenant

MLflow is available at `http://localhost:5050`. I use port 5050 because macOS may already use port
5000 for AirPlay.

## Try a search

Start the application, then load the sample products:

```bash
curl -X POST http://localhost:8000/demo/seed
```

Search the `demo-store` tenant:

```bash
curl -X POST http://localhost:8000/search \
  -H 'content-type: application/json' \
  -d '{"tenant_id":"demo-store","query":"portable developer laptop","limit":2}'
```

To run the current retrieval evaluation:

```bash
make evaluate
```

The evaluation currently contains three synthetic queries and scores Recall@1. That result only
checks this small test dataset; it is not meant to represent production retrieval quality.

## Next steps

The next milestone is to add public page and document ingestion, chunking experiments, a real
embedding model, hybrid search, and a larger evaluation set. Later milestones cover LangGraph,
human approval, gRPC, OpenTelemetry, MLflow evaluation, ML classification comparisons, and
cloud deployment.

The detailed plan is in [docs/ROADMAP.md](docs/ROADMAP.md). Verified results are kept separately in
[docs/EVIDENCE.md](docs/EVIDENCE.md), and architecture decisions are recorded in
[docs/adr](docs/adr).

## Data safety

This repository uses synthetic or public data only. It should not contain employer, client, medical,
financial, or other private information.
