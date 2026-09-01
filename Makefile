.PHONY: setup test lint run evaluate

setup:
	uv sync --extra dev

test:
	uv run pytest

lint:
	uv run ruff check src tests
	uv run mypy src

run:
	uv run uvicorn app.main:app --app-dir src --reload

evaluate:
	uv run python -m app.evaluation
