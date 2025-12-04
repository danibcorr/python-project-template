# Python Project Template Documentation

## Overview

The **Python Project Template** provides a fully structured foundation for Python
projects, integrating modern tooling for code quality, static analysis, security
auditing, testing, documentation, and development automation. It enables consistent,
maintainable, and reproducible workflows, streamlining project setup and encouraging
adherence to best practices.

This template is suitable for libraries, applications, and collaborative projects,
ensuring a professional development environment from the start.

## Project Structure and Core Components

### Makefile

The Makefile defines reusable targets to automate common tasks, including installation,
cleaning, linting, testing, and documentation. Commands are executed via
`make <target>`.

#### `make install`

Installs all project dependencies using [`uv`](https://github.com/astral-sh/uv), as
defined in `pyproject.toml`. Dependencies are organized into groups such as `pipeline`
and `documentation`, ensuring modular and selective installation.

#### `make clean`

Removes temporary and cache files to reset the workspace, including:

- Python bytecode (`.pyc`, `.pyo`)
- Cache directories: `__pycache__`, `.pytest_cache`, `.mypy_cache`

This ensures a clean state for linting, testing, and analysis.

#### `make lint`

Uses [Ruff](https://docs.astral.sh/ruff/) to automatically format and statically analyze
code. Linting is applied to source and test directories to enforce consistent coding
standards.

#### `make code_check`

Performs deeper analysis and security checks, including:

- **Mypy**: Validates type annotations and detects type inconsistencies.
- **Complexipy**: Measures code complexity to highlight potentially complicated logic.
- **Bandit**: Identifies common security issues in Python code.

This step ensures robust, maintainable, and secure code.

#### `make tests`

Runs unit tests with [Pytest](https://docs.pytest.org/en/stable/). The command exits
gracefully if no tests are detected, making it safe for partial or initial setups.

#### `make doc`

Serves the project documentation locally using [MkDocs](https://www.mkdocs.org/),
enabling live previews before deployment.

#### `make pipeline`

Executes a full quality pipeline comprising:

- Environment cleanup
- Linting and formatting
- Static analysis and security checks
- Test execution

This target is ideal for continuous integration and pre-release validation.

#### `make all`

Performs the complete workflow:

- Installs dependencies
- Runs the full quality pipeline
- Builds and serves documentation

Recommended for initial setup and full-cycle verification.

## pyproject.toml

Defines project metadata, dependency groups, and tool configurations in alignment with
modern Python standards.

### `[project]`

Specifies metadata such as:

- Project name, version, and description
- Python version compatibility
- Runtime dependencies

Conforms to [PEP 621](https://peps.python.org/pep-0621/) standards.

### `[dependency-groups]`

Organizes development dependencies into logical groups:

- **`pipeline`**: Tools for code analysis, linting, testing, and security checks:
  - `pytest`, `pytest-order`, `ruff`, `mypy`, `bandit`, `complexipy`
- **`documentation`**: Tools for building and extending documentation:
  - `mkdocs-material`, `mkdocstrings`, `mkdocs-jupyter`, and related plugins

This allows selective installation, improving modularity and manageability.

### `[tool.ruff]`

Configures Ruff for linting and formatting:

- Line length and indentation rules
- Linting rules and error detection
- Excluded directories (e.g., `venv`, `dist`, `.pytest_cache`)
- Formatting settings for docstrings and imports

### `[tool.mypy]`

Configures Mypy for static type checking:

- Checks untyped functions
- Ignores unresolved imports to handle missing stubs
- Excludes build and cache directories

This ensures early detection of type-related issues.

## GitHub Actions CI/CD

The template includes a preconfigured GitHub Actions workflow located in
`.github/workflows`. It runs automatically on pushes or pull requests and performs the
following steps:

1. **Checkout and Python Setup** – Clones the repository and configures the Python
   environment.
2. **Install Dependencies** – Installs all required packages for development, testing,
   and documentation.
3. **Linting and Static Analysis** – Runs Ruff, Mypy, Bandit, and Complexipy to enforce
   code quality, type safety, security, and complexity standards.
4. **Testing** – Executes Pytest to validate functionality and detect regressions.
5. **Documentation** – Optionally builds and deploys documentation with MkDocs to GitHub
   Pages.

This workflow ensures every code change is automatically validated, tested, and
documented.
