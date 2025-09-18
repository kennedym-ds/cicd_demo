# Development Commands

.PHONY: help install test lint format clean docs

help:  ## Show this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install:  ## Install project dependencies
	poetry install
	poetry run pre-commit install

test:  ## Run tests with coverage
	poetry run pytest --cov=src/python_cicd_demo --cov-report=html --cov-report=term-missing

lint:  ## Run linting and security checks
	poetry run black --check src tests
	poetry run isort --check-only src tests
	poetry run bandit -r src/

format:  ## Format code with black and isort
	poetry run black src tests
	poetry run isort src tests

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

docs:  ## Build documentation
	cd docs && poetry run sphinx-build -b html source _build/html

docs-serve:  ## Serve documentation locally
	cd docs/_build/html && python -m http.server 8000

pre-commit:  ## Run pre-commit hooks on all files
	poetry run pre-commit run --all-files

build:  ## Build the package
	poetry build
