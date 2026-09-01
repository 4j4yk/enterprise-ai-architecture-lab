# Enterprise AI Architecture Lab - Agent Instructions

## Mission

Build a defensible enterprise AI reference implementation that demonstrates the skills required for Principal Digital Solutions Architect roles. This is a hands-on portfolio project, not a resume-claim generator.

## Read first

Before changing code, read in order:

1. `docs/HANDOFF.md`
2. `docs/ARCHITECTURE.md`
3. `docs/ROADMAP.md`
4. `docs/EVIDENCE.md`

## Operating rules

- Keep changes small, testable, and reversible.
- Never commit secrets, API keys, private client data, or proprietary documents.
- Use synthetic or explicitly public data only.
- Label the project as an independent reference implementation.
- Do not claim production scale. Record the actual environment and measured load.
- Every architectural choice must include rationale, alternatives, and tradeoffs.
- Add or update an ADR for material architecture decisions.
- Add tests with each behavior change.
- Maintain REST and gRPC contracts with backward compatibility.
- Instrument important paths for traces, metrics, latency, token use, retrieval quality, and failures.
- Require human approval before any simulated write or operational action.
- Update `docs/EVIDENCE.md` only after a capability is working and verified.
- Resume-ready statements must be derived from measured evidence, never planned work.

## Definition of done for a milestone

- Implementation runs locally from documented commands.
- Automated tests pass.
- Security and failure modes are documented.
- Evaluation or performance results are recorded when relevant.
- Architecture diagrams and ADRs reflect the implementation.
- README and handoff status are current.

## Commands

Use the project virtual environment and pinned dependencies. Expected commands after setup:

```bash
make setup
make test
make lint
make run
docker compose up -d
```

## Git workflow

- Work on focused branches.
- Use descriptive commits.
- Do not push, deploy, publish, or modify remote infrastructure without explicit user approval.
- Preserve user changes and unrelated files.
