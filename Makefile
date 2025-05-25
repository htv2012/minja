.PHONY: all test run lint clean docs

### Default target(s)
all: test docs

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix
	uv run mypy src

### Run unit tests
test: lint
	uv run pytest -s -v

### Generate documentations
docs:
	./docs/make-docs.sh

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv docs/build docs/generated-source src/minja/__pycache__ src/test/__pycache__

### Install this tool locally
install:
	uv tool install --upgrade .
