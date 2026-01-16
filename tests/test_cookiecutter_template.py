# Standard libraries
import json
import subprocess
from pathlib import Path

# 3pps
import pytest


@pytest.fixture
def template_dir() -> Path:
    """
    Get the template directory path.

    Returns:
        The absolute path to the cookiecutter template root
        directory.
    """

    return Path(__file__).parent.parent


@pytest.fixture
def cookiecutter_config() -> dict:
    """
    Load cookiecutter configuration.

    Returns:
        Dictionary containing the parsed cookiecutter.json
        configuration.
    """

    config_path = Path(__file__).parent.parent / "cookiecutter.json"
    return json.loads(config_path.read_text())


def test_cookiecutter_json_exists(template_dir: Path) -> None:
    """
    Test that cookiecutter.json exists.

    Args:
        template_dir: The absolute path to the cookiecutter template
            root directory.

    Returns:
        None
    """

    assert (template_dir / "cookiecutter.json").exists()


def test_cookiecutter_json_valid(cookiecutter_config: dict) -> None:
    """
    Test that cookiecutter.json is valid JSON with required fields.

    Args:
        cookiecutter_config: Dictionary containing the parsed
            cookiecutter.json configuration.

    Returns:
        None
    """

    required_fields = [
        "project_name",
        "project_module_name",
        "project_test_folder_name",
        "project_version",
    ]
    for field in required_fields:
        assert field in cookiecutter_config


def test_template_generation(tmp_path: Path, template_dir: Path) -> None:
    """
    Test that cookiecutter generates a valid project.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.

    Returns:
        None
    """

    result = subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            "--output-dir",
            str(tmp_path),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Failed: {result.stderr}"

    generated_project = tmp_path / "project-name"
    assert generated_project.exists()


def test_generated_project_structure(tmp_path: Path, template_dir: Path) -> None:
    """
    Test that generated project has correct structure.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.

    Returns:
        None
    """

    subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    project = tmp_path / "project-name"
    expected_files = [
        "pyproject.toml",
        "Makefile",
        "README.md",
        "mkdocs.yml",
        ".gitignore",
    ]

    for file in expected_files:
        assert (project / file).exists(), f"Missing {file}"


def test_generated_project_folders(tmp_path: Path, template_dir: Path) -> None:
    """
    Test that generated project has correct folders.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.

    Returns:
        None
    """

    subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    project = tmp_path / "project-name"
    expected_folders = ["src", "tests", "docs", "config"]

    for folder in expected_folders:
        assert (project / folder).exists(), f"Missing {folder}"


@pytest.mark.parametrize(
    "folder_option,folder_name",
    [
        ("add_dev_container_folder", ".devcontainer"),
        ("add_vscode_folder", ".vscode"),
        ("add_notebooks_folder", "notebooks"),
        ("add_prompts_folder", "prompts"),
    ],
)
def test_optional_folders_yes(tmp_path: Path, template_dir: Path, folder_option: str, folder_name: str) -> None:
    """
    Test that optional folders are created when enabled.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.
        folder_option: Cookiecutter configuration option name.
        folder_name: Name of the folder to verify.

    Returns:
        None
    """

    subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            f"{folder_option}=yes",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    project = tmp_path / "project-name"
    assert (project / folder_name).exists()


@pytest.mark.parametrize(
    "folder_option,folder_name",
    [
        ("add_dev_container_folder", ".devcontainer"),
        ("add_vscode_folder", ".vscode"),
        ("add_notebooks_folder", "notebooks"),
        ("add_prompts_folder", "prompts"),
    ],
)
def test_optional_folders_no(tmp_path: Path, template_dir: Path, folder_option: str, folder_name: str) -> None:
    """
    Test that optional folders are removed when disabled.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.
        folder_option: Cookiecutter configuration option name.
        folder_name: Name of the folder to verify.

    Returns:
        None
    """

    subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            f"{folder_option}=no",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    project = tmp_path / "project-name"
    assert not (project / folder_name).exists()


def test_generated_pyproject_valid(tmp_path: Path, template_dir: Path) -> None:
    """
    Test that generated pyproject.toml is valid.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.

    Returns:
        None
    """

    subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            "project_name=test-project",
            "project_module_name=test_module",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    pyproject = tmp_path / "test-project" / "pyproject.toml"
    content = pyproject.read_text()

    assert "test-project" in content
    assert "test_module" in content
    assert "[project]" in content
    assert "[tool.uv]" in content


def test_makefile_commands_exist(tmp_path: Path, template_dir: Path) -> None:
    """
    Test that Makefile has required commands.

    Args:
        tmp_path: Temporary directory path provided by pytest.
        template_dir: The absolute path to the cookiecutter template
            root directory.

    Returns:
        None
    """
    
    subprocess.run(
        [
            "uv",
            "run",
            "cookiecutter",
            str(template_dir),
            "--no-input",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    makefile = tmp_path / "project-name" / "Makefile"
    content = makefile.read_text()

    required_commands = ["setup", "lint", "code-check", "tests", "pipeline"]
    for cmd in required_commands:
        assert f"{cmd}:" in content, f"Missing command: {cmd}"

    assert "uv sync" in content or "uv run" in content
