# Pre-Commit Hooks

## Overview

Pre-commit hooks are automated scripts configured to execute specific validations before
a Git commit is finalized. In this project, the pre-commit system is defined in the
`.pre-commit-config.yaml` file. Its primary purpose is to enforce code quality, detect
potential errors early, and prevent non-compliant code from entering the repository. By
integrating pre-commit hooks into the workflow, the project ensures that all committed
changes meet established coding standards and pass essential checks automatically.

## Functionality

When a developer attempts to commit changes, the pre-commit system automatically triggers
the pre-commit validation pipeline by executing:

```bash
make pre-commit
```

This command performs a comprehensive sequence of actions, including:

- Linting and formatting checks to ensure consistent code style.
- Type validation using Mypy to detect mismatches and type-related errors.
- Security analysis with Bandit to identify potential vulnerabilities in the code.
- Complexity analysis with Complexipy to identify overly complex code.

If any of these checks fail, the commit is blocked, thereby preventing problematic code
from being added to the repository. Note that tests are not executed during pre-commit to
keep the validation fast, but they are run in the full `make pipeline` command.

## Advantages

Integrating pre-commit hooks into the development workflow provides several key benefits:

- **Quality Enforcement**: Only code that passes all validations can be committed,
  maintaining a high standard across the codebase.
- **Early Issue Detection**: Errors are detected before code is pushed or reviewed,
  reducing downstream debugging and rework.
- **Clean Git History**: By preventing commits that violate coding standards or fail
  tests, the repository maintains a cleaner and more reliable history.

## Temporary Bypass (Not Recommended)

While it is possible to bypass pre-commit validations using the `--no-verify` flag:

```bash
git commit --no-verify -m "commit message"
```

this approach is discouraged because it undermines the automated quality safeguards and
may introduce errors or inconsistencies into the codebase. Pre-commit hooks are intended
to be an integral part of the workflow, ensuring that each commit contributes to a
robust, secure, and maintainable project.
