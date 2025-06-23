# 🐍 Python Project Template

Welcome to the Python Project Template — your go-to starter kit for building robust
Python projects with clean code, strong testing, built-in security, and automated
deployment. Whether you're launching a new idea or refining your workflow, this template
sets you up for success.

## What's Inside

- **Linting & Type Checking**: Keep your code clean with
  [Ruff](https://docs.astral.sh/ruff/) and [Mypy](http://mypy-lang.org/).
- **Security Scanning**: Catch vulnerabilities early using
  [Bandit](https://bandit.readthedocs.io/en/latest/).
- **Code Complexity Analysis**: Understand your codebase with
  [Complexipy](https://rohaquinlop.github.io/complexipy/).
- **Testing Suite**: Reliable testing with [Pytest](https://docs.pytest.org/en/stable/).
- **Auto Documentation**: Generate and deploy docs with
  [MkDocs](https://www.mkdocs.org/) + [GitHub Pages](https://pages.github.com/).
- **CI/CD**: Automate your workflow using GitHub Actions — from linting and testing to
  doc deployment.

And more...

## Getting Started

### 1. Generate Your Project

Activate your Python environment, install `cookiecutter`, and run:

```bash
cookiecutter https://github.com/danibcorr/python-project-template.git
```

### 2. Install Dependencies

Use the included `Makefile`:

```bash
make install
```

### 3. Run the Pipeline

Lint, test, and check your project:

```bash
make pipeline
```

Or run the full suite including docs:

```bash
make all
```

## Contributing

We welcome contributions from the community! To get started quickly, follow these steps
using our streamlined `Makefile`:

1. **Clone the repository** Ensure your system is updated and `make` is installed. On
   most Linux systems:

   ```bash
   sudo apt-get update
   sudo apt-get install build-essential
   ```

2. **Set up your environment** Navigate to the cloned directory, create a Python
   environment, activate it, and run:

   ```bash
   make
   ```

   This command updates `pip`, installs `uv`, and sets up all project dependencies
   automatically.
