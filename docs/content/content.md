# Python Project Template Documentation

## Overview

The **Python Project Template** provides a comprehensive and structured foundation for
Python projects, integrating modern tooling to ensure code quality, static analysis,
security auditing, testing, documentation, and development automation. The template
promotes consistent, maintainable, and reproducible workflows, streamlining project
setup and enforcing adherence to established best practices.

This framework is suitable for libraries, applications, and collaborative projects,
establishing a professional development environment from the outset.

## Project Structure and Core Components

### Makefile

The Makefile defines reusable targets to automate common development tasks, including
dependency installation, workspace cleanup, linting, testing, static and security
analysis, and documentation management. Commands are executed using the syntax
`make <target>`.

#### `make install`

Installs all project dependencies using [`uv`](https://github.com/astral-sh/uv) as
defined in `pyproject.toml`. Dependencies are organized into modular groups such as
`pipeline` and `documentation`, enabling selective installation according to the
required development context.

#### `make clean`

Removes temporary and cache files to restore a clean workspace. This includes Python
bytecode files (`.pyc`, `.pyo`) and cache directories such as `__pycache__`,
`.pytest_cache`, and `.mypy_cache`. Performing this step ensures reliable results for
linting, testing, and static analysis by eliminating residual artifacts from previous
runs.

#### `make lint`

Executes [Ruff](https://docs.astral.sh/ruff/) to enforce code formatting and static
analysis rules across source and test directories. This target promotes consistent
coding standards and prevents stylistic inconsistencies.

#### `make code_check`

Performs advanced code validation and security assessments, including:

- **Mypy**: Validates type annotations and identifies type inconsistencies.
- **Complexipy**: Measures code complexity, highlighting potentially intricate or
  hard-to-maintain logic.
- **Bandit**: Conducts static security analysis (SAST) to detect common vulnerabilities
  and security issues within Python code.

This step ensures that the codebase remains robust, maintainable, and secure.

#### `make tests`

Runs unit tests using [Pytest](https://docs.pytest.org/en/stable/). The command exits
gracefully if no tests are detected, making it suitable for partial implementations or
early-stage project setups.

#### `make doc`

Builds and serves project documentation locally with [MkDocs](https://www.mkdocs.org/),
allowing developers to preview documentation changes in real time before deployment.

#### `make pipeline`

Executes a complete quality pipeline that includes environment cleanup, linting, static
analysis, security checks, and test execution. This target is designed for continuous
integration workflows and pre-release verification.

#### `make all`

Performs the full project workflow, encompassing dependency installation, execution of
the full quality pipeline, and documentation build and preview. This target is
recommended for initial project setup and comprehensive workflow verification.

### `pyproject.toml`

The `pyproject.toml` file defines project metadata, dependency groups, and tool
configurations in accordance with modern Python standards.

#### `[project]`

Specifies core project metadata, including project name, version, description, Python
version compatibility, and runtime dependencies. This section adheres to
[PEP 621](https://peps.python.org/pep-0621/) standards.

#### `[dependency-groups]`

Organizes development dependencies into logical groups to enable modular installation:

- **`pipeline`**: Includes tools for code quality, testing, and security assessment,
  such as `pytest`, `pytest-order`, `ruff`, `mypy`, `bandit`, and `complexipy`.
- **`documentation`**: Contains tools for building and enhancing documentation,
  including `mkdocs-material`, `mkdocstrings`, `mkdocs-jupyter`, and related plugins.

This modular approach improves maintainability and flexibility of the development
environment.

#### `[tool.ruff]`

Configures Ruff for code linting and formatting, including rules for line length,
indentation, error detection, and docstring formatting. Certain directories, such as
`venv`, `dist`, and `.pytest_cache`, are excluded to optimize performance.

#### `[tool.mypy]`

Configures Mypy for static type checking. It enables detection of untyped functions,
ignores unresolved imports to accommodate missing type stubs, and excludes build and
cache directories. This configuration allows early detection of type-related errors,
improving code reliability.

## GitHub Actions CI/CD

The template includes a preconfigured GitHub Actions workflow located in
`.github/workflows`. This workflow is triggered automatically on pushes or pull requests
and performs the following steps:

1. **Checkout and Python Setup** – Clones the repository and configures the Python
   environment.
2. **Dependency Installation** – Installs all required packages for development,
   testing, and documentation.
3. **Linting and Static Analysis** – Executes Ruff, Mypy, Bandit, and Complexipy to
   enforce code quality, type safety, security, and maintainability.
4. **Testing** – Runs Pytest to validate functionality and detect regressions.
5. **Documentation** – Optionally builds and deploys project documentation to GitHub
   Pages using MkDocs.

This workflow ensures that all code changes are automatically validated, tested, and
documented, supporting continuous integration and promoting high-quality software
development practices.
