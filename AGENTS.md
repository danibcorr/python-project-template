# Agent Instructions

This is a **Cookiecutter template** for generating Python projects with integrated best
practices for code quality, testing, security, documentation, and CI/CD.

## Before You Start

1. Review `README.md` for template overview and features
2. Check `AGENTS.md` in generated projects for project-specific instructions
3. Understand this is a **dynamic generator**, not a static project

## Key Files

- **cookiecutter.json**: Template variables (metadata, Python version, optional features)
- **hooks/post_gen_project.py**: Removes disabled optional folders post-generation
- **Makefile**: Workflow commands (`setup`, `lint`, `code-check`, `test`, `pipeline`)
- **.github/actions/**: Reusable GitHub Actions for CI/CD

## Template Syntax

- Files use **Jinja2 syntax**: `{{ cookiecutter.project_name }}`
- Preserve template delimiters and conditional blocks when modifying
- Invalid syntax breaks project generation

## Validation Workflow

Run `make pipeline` to execute:

- Linting (Ruff, isort)
- Type checking (Mypy)
- Complexity analysis (Complexipy)
- Security scanning (Bandit)
- Tests (Pytest)

## Critical Rules

1. This generates projects; each instance differs based on `cookiecutter.json` choices
2. Optional features: `.devcontainer/`, `.vscode/`, `notebooks/`, `prompts/`
3. Always validate changes with `make pipeline`
4. Never break Jinja2 template syntax
