# Contributing to Python Project Template

Thank you for your interest in contributing to the **Python Project Template**.
Contributions of all types are welcome, including code, documentation, bug reports, and
feature requests. This guide outlines the recommended workflow for contributing
effectively.

## Joining the Project

If you are interested in contributing or collaborating more closely, feel free to reach
out to the maintainers.

## Ways to Contribute

You can contribute by:

- Reporting bugs or requesting new features.
- Submitting code contributions, including bug fixes, improvements, or new features.

> Note: While we strive to respond promptly, we cannot guarantee an immediate reply due
> to the number of projects we maintain.

## Contributing Code

### Step 1: Open an Issue

Start by opening an issue to describe your proposed change or the problem you
encountered. This helps maintainers review and guide the work before coding begins.

> For minor changes, such as typo fixes, you may skip this step and submit a pull
> request directly.

### Step 2: Make Your Changes

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch for your changes.
4. Set up your development environment (see [Setup Environment](#setup-environment)).
5. Implement your changes and ensure all tests pass.

### Step 3: Submit a Pull Request

Open a pull request (PR) from your branch to the `main` branch of the repository.

### Step 4: Code Review

A maintainer will review your PR and may provide feedback. You might be asked to:

- Revise code for correctness or clarity
- Adjust formatting
- Improve test coverage

> Address any review comments and ensure all tests pass before requesting a re-review.

### Step 5: Merge

After approval, a maintainer will merge your pull request.

## Setup Environment

You can set up the development environment in one of two ways:

### Option 1: Dev Container

We support development containers for Visual Studio Code, GitHub Codespaces, and
JetBrains IDEs. This provides a preconfigured environment for immediate work.

### Option 2: Local Setup

To set up locally:

1. Ensure `git` and Python (3.10, 3.11, or 3.12) are installed.
2. Optionally, install [`uv`](https://github.com/astral-sh/uv) to manage dependency
   groups.
3. Clone the repository and run:

```bash
make install
```

> If using `uv`, a compatible virtual environment will be created automatically.

## Running Tests

All tests are run using [pytest](https://docs.pytest.org/):

```bash
make tests
```

## Code Formatting & Quality Checks

Use `make` to automate formatting, linting, static analysis, testing, and documentation:

```bash
make
```

This executes:

- Dependency installation
- Linters (`ruff`, `black`, `isort`)
- Static analysis (`complexipy`, `mypy`, `bandit`)
- Test suite execution
- Local documentation preview

## Docstring Guidelines

Function docstrings should include:

- A concise one-line description
- Optional detailed explanation
- `Args:` section describing parameters
- `Returns:` section
- Optional `Raises:` section for exceptions
- Optional `Examples:` section demonstrating usage

Maintain clarity, consistency, and completeness in docstrings.

## Other Ways to Contribute

Non-code contributions are highly valuable, including:

- Improving documentation or examples
- Fixing typos and grammar issues
- Suggesting features or enhancements
- Assisting with issue triage and responses

Thank you for contributing to the Python Project Template. Your participation helps
improve the project for everyone. If you have questions, feel free to reach out or open
an issue.
