# Verified Evidence Ledger

Only record completed, reproducible evidence here.

## Rules

- Planned work is not evidence.
- Include the command, test, report, commit, or live URL that verifies each claim.
- Include the test environment and dataset size for every metric.
- Do not generalize a local demo into a production-scale claim.

## Evidence table

| Capability | Status | Verification | Measured result | Resume-safe wording |
|---|---|---|---|---|
| Local API foundation | Verified locally | `pytest`, `ruff`, `mypy`, `docker compose config`, dependency check | 3 tests passed; PostgreSQL, Qdrant, and MLflow reachable on a developer Mac | Built a tested local FastAPI foundation with dependency readiness checks and containerized supporting services |
| Synthetic catalog ingestion | Verified locally | `tests/test_catalog.py` | 3 synthetic products normalized | Built a tested adapter that normalizes synthetic commerce records into tenant-aware documents |
| Qdrant vector retrieval | Verified locally | `tests/test_retrieval.py`, `python -m app.evaluation` | Recall@1 = 1.00 on 3 synthetic queries; tenant isolation test passed | Implemented tenant-filtered Qdrant vector retrieval with citations and a reproducible evaluation baseline |
| LangGraph durable workflow | Not started | - | - | - |
| Human approval | Not started | - | - | - |
| gRPC service | Not started | - | - | - |
| MLflow evaluation | Not started | - | - | - |
| OpenTelemetry | Not started | - | - | - |
| Classical ML benchmark | Not started | - | - | - |
| Snowflake POC | Not started | - | - | - |

## Verification log

### 2026-09-01 - Milestone 0 foundation

- Environment: local macOS workstation, Python 3.13.5, Docker Compose.
- `uv sync --locked --extra dev`: installed the locked environment.
- `.venv/bin/pytest`: 3 tests passed.
- `.venv/bin/ruff check src tests`: passed.
- `.venv/bin/mypy src`: passed.
- `docker compose config --quiet`: passed.
- Runtime dependency check: PostgreSQL, Qdrant, and MLflow all reachable.
- Scope limit: no load, retrieval-quality, reliability, or production-scale claim was measured.

### 2026-09-01 - Retrieval baseline

- Environment: in-memory Qdrant test client and live local Qdrant container.
- Dataset: 3 synthetic products and 3 synthetic evaluation queries.
- Result: Recall@1 = 1.00; tenant boundary and citation tests passed.
- End-to-end API: seeded 3 documents and returned the expected laptop as rank 1.
- Scope limit: the deterministic hash embedding is a baseline and does not demonstrate semantic
  model quality or production scale.

## Resume update gate

A capability may be added to the resume only when it has:

1. Working code.
2. Automated verification.
3. Documentation.
4. A reproducible or measured result.
5. Accurate scope language.
