# Makefile

## Overview

The project includes a `Makefile` designed to automate routine development tasks. Each
command is executed using the syntax `make <command>` and encapsulates a sequence of
actions that standardize workflows, enforce code quality, and simplify maintenance. By
centralizing these tasks, the `Makefile` ensures consistency across development
environments and reduces manual errors.

## Environment Setup: `make setup`

The `setup` command installs all necessary dependencies and configures pre-commit hooks
to enforce code standards automatically. It leverages `uv`, a high-performance Python
package manager, to install the required packages efficiently. Dependency groups include
`pipeline`, which contains tools for testing and linting, and `documentation`, which
includes MkDocs for building project documentation. Pre-commit hooks are configured to
validate code before each commit, preventing common errors and maintaining quality. This
command should be executed the first time the project is cloned or whenever dependencies
are updated.

```bash
make setup
```

## Cleaning Temporary Files: `make clean-cache-temp-files`

This command removes temporary files and caches that may cause inconsistencies or errors
during development. Specifically, it deletes compiled Python bytecode (`__pycache__/`),
pytest caches (`.pytest_cache/`), mypy caches (`.mypy_cache/`), and other compiled files
such as `*.pyc` and `*.pyo`. Regular use of this command ensures a clean environment,
particularly before running the complete pipeline or debugging unusual behavior.

```bash
make clean-cache-temp-files
```

## Code Formatting and Automatic Fixes: `make lint`

The `lint` command enforces coding standards and applies automatic fixes to improve code
readability and maintainability. It integrates several tools:

- **isort**: Organizes imports alphabetically and categorically.
- **Ruff**: A high-performance linter that detects and fixes style issues.

Typical automatic fixes include removing unused imports, correcting spacing and
formatting, and reorganizing imports according to PEP 8 conventions. This command is
recommended before committing code or when performing routine code cleanup.

```bash
make lint
```

## Static and Security Analysis: `make code-check`

The `code-check` command performs an in-depth analysis to identify potential issues in
the codebase. It combines multiple tools:

1. **Mypy**: A static type checker that validates type annotations and detects mismatched
   types before runtime.
2. **Complexipy**: Measures cyclomatic complexity to identify functions that may be
   difficult to maintain or require refactoring.
3. **Bandit**: Conducts static application security testing (SAST) to identify common
   vulnerabilities, such as SQL injection risks, unsafe `eval()` usage, and hardcoded
   credentials. It scans all code excluding test directories.

This command is essential before merging changes into the main branch or during code
reviews to ensure robust, maintainable, and secure code.

```bash
make code-check
```

## Dead Code Detection: `make check-dead-code`

The `check-dead-code` command identifies unused or redundant code that can be safely
removed. It detects functions that are never called, uninstantiated classes, and
variables that are defined but not utilized. Running this command is particularly useful
during refactoring or when optimizing the codebase for maintainability.

```bash
make check-dead-code
```

## Running Unit Tests: `make tests`

This command executes all unit tests using Pytest. It supports structured test execution
via `pytest-order` and can generate coverage reports if configured. The `tests/`
directory is scanned recursively, ensuring that all modules are tested thoroughly. This
command should be run frequently after code modifications to verify correctness.

```bash
make tests
```

## Documentation Management: `make doc`

The `doc` command builds and serves project documentation locally using MkDocs. It
launches a development server (by default accessible at `http://127.0.0.1:8000`) and
automatically reloads pages when Markdown files are updated. This allows developers to
preview documentation as it will appear on GitHub Pages and ensures consistency between
local edits and published content.

```bash
make doc
```

## Complete Code Quality Pipeline: `make pipeline`

The `pipeline` command orchestrates the full sequence of code quality checks and testing.
It sequentially:

1. Cleans caches and temporary files.
2. Runs linting and formatting.
3. Performs static analysis, complexity measurement, and security scanning.
4. Executes all unit tests.

This command is particularly useful before pushing changes to the repository or as part
of a continuous integration (CI) workflow.

```bash
make pipeline
```

## Full Workflow Execution: `make all`

The `all` command executes the complete project setup and validation workflow. It
installs dependencies, runs the full code quality pipeline, and serves the documentation
locally. This command provides a comprehensive initialization process, ensuring the
development environment is fully configured and all systems are validated.

```bash
make all
```
