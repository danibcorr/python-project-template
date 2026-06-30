# Cookiecutter

## Introduction to Cookiecutter

Cookiecutter is a command-line utility designed to generate project structures from
predefined templates. It enables developers to rapidly scaffold new projects by
prompting for configuration inputs and customizing the generated files according to the
provided responses. This approach ensures consistency across projects, reduces setup
time, and enforces best practices and organizational standards in project structure.

## Configuration Variables

The customization process is driven by a configuration file, `cookiecutter.json`, which
defines the variables that the template expects. Each variable corresponds to a specific
aspect of the project, such as naming conventions, folder structures, or optional
features. During project generation, Cookiecutter interactively prompts the user to
provide values for these variables, thereby producing a project tailored to the user’s
specifications. The main configuration variables include:

| Variable                    | Description                                                     | Example                        |
| --------------------------- | --------------------------------------------------------------- | ------------------------------ |
| `project_authors`           | Full name of the project author(s)                              | `Your Name`                    |
| `project_authors_email`     | Contact email address of the author(s)                          | `your.email@example.com`       |
| `project_name`              | Name of the project (used as directory and package identifier)  | `my-project`                   |
| `project_module_name`       | Name of the Python source module                                | `src`                          |
| `project_test_folder_name`  | Name of the folder for tests                                    | `tests`                        |
| `project_short_description` | Short, one-line description of the project's purpose            | `What this project does.`      |
| `project_version`           | Initial semantic version of the project                         | `0.0.1`                        |
| `project_version_python`    | Minimum required Python version                                 | `3.11`                         |
| `project_license`           | SPDX license identifier (selection list)                        | `MIT`                          |
| `site_name`                 | Title of the generated documentation site                       | `Project Title`                |
| `repo_url`                  | URL of the repository for documentation cross-links             | `https://github.com/user/repo` |
| `site_url`                  | Base URL where the documentation is published                   | `https://user.github.io/repo/` |
| `add_vscode_folder`         | Whether to include VS Code workspace configuration (`.vscode/`) | `yes` / `no`                   |
| `add_notebooks_folder`      | Whether to include a Jupyter notebooks folder                   | `yes` / `no`                   |
| `add_prompts_folder`        | Whether to include a prompts folder for LLM or agent use cases  | `yes` / `no`                   |

These variables enable fine-grained control over the structure and functionality of the
generated project, accommodating different workflows and development environments.

## Project Generation Workflow

The process of generating a project using Cookiecutter is straightforward. The user
executes the `cookiecutter` command with the URL or local path of the desired template
repository. Cookiecutter then sequentially prompts the user to provide values for each
configuration variable defined in `cookiecutter.json`. Once all responses are collected,
the tool automatically creates a new project directory populated with files and folders
customized according to the provided inputs.

For example, executing:

```bash linenums="1"
uvx cookiecutter https://github.com/danibcorr/python-project-template.git
```

initiates the generation process. The user answers the interactive prompts, specifying
names, versions, and optional components. Upon completion, a fully scaffolded project
appears, reflecting the selected options and ready for immediate development. This
automated approach promotes reproducibility, reduces setup errors, and enforces a
consistent organizational structure across multiple projects.
