# Contributing to SureHub API

Thank you for taking the time to contribute! The following guidelines help keep the process smooth for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Reporting Issues](#reporting-issues)
- [Submitting Changes](#submitting-changes)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Commit Messages](#commit-messages)

## Code of Conduct

Be respectful and constructive. Harassment or abusive behavior will not be tolerated.

## Getting Started

1. **Fork** the repository and create your branch from `main`.
2. Follow the [Development Setup](#development-setup) steps below.
3. Make your changes, add tests where appropriate, and ensure all tests pass.
4. Open a **Pull Request** against `main`.

For significant changes, open an issue first to discuss your approach before investing time in an implementation.

## Reporting Issues

Use [GitHub Issues](https://github.com/fabieu/surehub-api/issues) to report bugs or request features.

For **security vulnerabilities**, follow the [Security Policy](SECURITY.md) instead — do not open a public issue.

When filing a bug report include:

- SureHub API version (`docker inspect` image label or `pyproject.toml`)
- How you installed/run the API (Docker or manual)
- Steps to reproduce
- Expected vs. actual behaviour
- Relevant log output (`SUREHUB_LOGLEVEL=debug`)

## Submitting Changes

- Keep PRs focused — one feature or fix per PR.
- Reference related issues in the PR description (`Closes #123`).
- Update documentation (README, OpenAPI annotations) if your change affects behaviour or configuration.
- All CI checks must pass before a PR can be merged.

## Development Setup

**Prerequisites:** Python ≥ 3.10, [Poetry](https://python-poetry.org/)

```bash
git clone https://github.com/fabieu/surehub-api.git
cd surehub-api

# Install dependencies (including dev group)
poetry install

# Activate the virtual environment
poetry shell

# Copy and configure environment variables
export SUREHUB_EMAIL=your@email.com
export SUREHUB_PASSWORD=yourpassword

# Run the API locally
poetry run python surehub_api/main.py
```

**Docker (alternative):**

```bash
docker compose up --build
```

## Testing

Run the test suite with:

```bash
poetry run pytest
```

- Add or update tests for any changed behaviour.
- Tests live in the `tests/` directory and mirror the `surehub_api/` structure.
- Check minimum Python version compatibility:
  ```bash
  poetry run vermin surehub_api/
  ```

### Contract tests

`tests/contract/` contains live tests against the real Sure Petcare API that:

- Validate every read-only endpoint's response against its Pydantic model (catches breaking type/required-field changes).
- Diff the raw response *structure* against a committed snapshot in `tests/contract/snapshots/` to detect added, removed, or renamed fields that Pydantic alone wouldn't flag.

They require `SUREHUB_EMAIL`/`SUREHUB_PASSWORD` and are skipped automatically otherwise. They also run on a daily schedule via [`contract-tests.yml`](.github/workflows/contract-tests.yml) and fail the workflow if Sure Petcare's API contract has changed. See [`tests/contract/snapshots/README.md`](tests/contract/snapshots/README.md) for how to review and accept such changes.

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`

Examples:

```
feat(devices): add support for feeder lid status
fix(auth): handle expired session tokens gracefully
docs(readme): update Docker image registry reference
```
