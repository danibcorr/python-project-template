# Agent Instructions

This is a **Cookiecutter template** for generating Python projects with integrated best
practices for code quality, testing, security, documentation, and CI/CD.

## Before You Start

1. Review `README.md` for template overview and features
2. Check `AGENTS.md` in generated projects for project-specific instructions
3. Understand this is a **dynamic generator**, not a static project

## Key Files

- **cookiecutter.json**: Template variables (metadata, Python version, optional
  features)
- **hooks/post_gen_project.py**: Removes disabled optional folders post-generation
- **Makefile**: Root-repository workflow commands (see targets below)
- **`{{ cookiecutter.project_name }}/Makefile`**: Makefile embedded in the template,
  copied verbatim into every generated project
- **.github/actions/**: Reusable GitHub Actions for CI/CD

## Template Syntax

- Files use **Jinja2 syntax**: `{{ cookiecutter.project_name }}`
- Preserve template delimiters and conditional blocks when modifying
- Invalid syntax breaks project generation

## Root Makefile Targets

The root `Makefile` operates on the template repository itself, not on generated
projects. Its targets are:

| Target                        | Description                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------ |
| `make setup`                  | Installs dependencies via `uv sync --all-extras`                               |
| `make clean-cache-temp-files` | Removes `__pycache__`, `.pytest_cache`, `.mypy_cache`, and compiled bytecode   |
| `make code-check`             | Runs Mypy (type checking) and Complexipy (complexity analysis)                 |
| `make test`                   | Executes Pytest against the `tests/` directory                                 |
| `make format`                 | Formats all files with Prettier (`npx prettier --write .`)                     |
| `make doc`                    | Serves documentation locally via `uv run zensical serve`                       |
| `make pipeline`               | Sequentially runs: `clean-cache-temp-files` → `format` → `code-check` → `test` |
| `make all`                    | Runs `setup`, then `pipeline`, then `doc`                                      |

> **Note**: The root Makefile does **not** include `lint`, `ruff`, `isort`, `bandit`,
> `check-dead-code`, or `pre-commit` targets. Those tools exist only in the Makefile
> generated inside each project (`{{ cookiecutter.project_name }}/Makefile`), where
> `make lint` runs isort and Ruff, `make code-check` additionally runs Bandit, and
> `make pipeline` chains `lint` → `code-check` → `test`.

## Validation Workflow

Run `make pipeline` to execute the root template validation:

- Code formatting (Prettier)
- Type checking (Mypy)
- Complexity analysis (Complexipy)
- Tests (Pytest)

## Critical Rules

1. This generates projects; each instance differs based on `cookiecutter.json` choices
2. Optional features: `.vscode/`, `notebooks/`, `prompts/`
3. Always validate template-level changes with `make pipeline` (root Makefile)
4. Never break Jinja2 template syntax
5. Changes to `{{ cookiecutter.project_name }}/Makefile` affect every generated project
