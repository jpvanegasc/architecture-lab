.DEFAULT_GOAL := help

.SILENT:

.env:
	cp .sample.env .env

.PHONY:

init: .env
	uv sync
	uv run pre-commit install

lint: ## Run linters via pre-commit
	uv run pre-commit run --all-files

test: ## Run tests
	APIURL=http://localhost:8000 bash tests/run-api-tests.sh

help: ## Show this help message
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
