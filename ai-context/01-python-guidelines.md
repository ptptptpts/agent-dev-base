# Professional Python Development Guidelines

## Package & Dependency Management
- **Primary Tool**: Use `uv` for lightning-fast dependency management and virtual environments.
- **Project Setup**: Use `pyproject.toml` as the single source of truth for project metadata and dependencies.

## Data Validation & Type Safety
- **Pydantic**: Use Pydantic V2 for data validation, settings management, and defining clear data schemas.
- **Type Hints**: Mandatory for all function signatures. Use `typing.Annotated` for enhanced metadata where useful.

## Architectural Patterns
- **Functional & Procedural**: Prefer pure functions for logic.
- **Structured Logging**: Use `structlog` or standard `logging` with JSON formatters for observability.
- **Custom Exceptions**: Define a hierarchy of domain-specific exceptions for granular error handling.

## Testing & Quality
- **Pytest**: Use `pytest` with `pytest-asyncio` for asynchronous code.
- **Fixtures**: Utilize reusable fixtures in `conftest.py` to keep tests DRY.
- **Ruff**: Use `ruff` for extremely fast linting and formatting (replaces Flake8, Black, isort).
