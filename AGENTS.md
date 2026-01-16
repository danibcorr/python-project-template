# Agent Instructions

This project is a **Cookiecutter template** used to generate new Python projects with a
professional, ready-to-use structure. It integrates best practices for code quality,
testing, security, documentation, and CI/CD. Because it is highly dynamic, it includes
many optional settings and Jinja2 template blocks.

## Getting Context

Before interacting with the template, make sure to:

1. **Review the README**: The `README.md` provides a high-level overview of the template,
   its features, CI/CD workflow, and instructions to generate new projects. Key features
   include:

   - Linting & type checking (Ruff & Mypy)
   - Security scanning (Bandit)
   - Code complexity analysis (Complexipy)
   - Testing (Pytest)
   - Auto documentation (MkDocs + GitHub Pages)
   - Preconfigured GitHub Actions for CI/CD

2. **Review `AGENTS.md` in the generated project**: After generating a new project, the
   template copies an `AGENTS.md` file to the project itself
   (`{{cookiecutter.__package_slug}}/AGENTS.md`). This file provides project-specific
   instructions for agents.

## Working with the Template

- **Jinja2 blocks**: Because this is a Cookiecutter template, many files contain Jinja2
  template syntax. Agents should expect template variables like
  `{{ cookiecutter.project_name }}` or conditional blocks.

- **Testing functionality**:

  - Create new projects inside the `workspaces/` directory.
  - Run the Makefile targets to validate functionality:

    - `make setup` → installs dependencies
    - `make pipeline` → runs linting, type checking, security analysis, complexity
      checks, and tests
    - `make all` → full workflow including documentation preview

  - Ensure the environment is isolated (e.g., via `venv`) and that
    [`uv`](https://github.com/astral-sh/uv) is installed to handle grouped dependency
    installations.

## Summary

Agents interacting with this template should:

- Understand it is a **dynamic project generator**, not a single static project.
- Always use the generated `workspaces/` directory for testing.
- Follow the Makefile workflow to validate and test features.
- Keep track of optional components and ensure `post_gen_project.py` handles cleanup
  properly.

By following these instructions, agents will be able to safely generate, test, and
maintain projects derived from this Python template.
