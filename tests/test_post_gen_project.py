# Standard libraries
from pathlib import Path
from unittest.mock import patch

# 3pps
import pytest

# Own modules
from hooks.post_gen_project import remove


@pytest.fixture
def mock_project_dir(tmp_path: Path) -> Path:
    """
    Create a temporary project directory with test folders.

    Generates a mock project structure containing the standard
    optional folders (.devcontainer, .vscode, notebooks, prompts)
    with a test file in each.

    Args:
        tmp_path: Temporary directory path provided by pytest.

    Returns:
        The path to the temporary project directory.
    """

    folders = [".devcontainer", ".vscode", "notebooks", "prompts"]
    for folder in folders:
        (tmp_path / folder).mkdir()
        (tmp_path / folder / "test.txt").write_text("test")

    return tmp_path


def test_remove_file(tmp_path: Path) -> None:
    """
    Test removing a file.

    Args:
        tmp_path: Temporary directory path provided by pytest.

    Returns:
        None
    """

    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    assert test_file.exists()

    remove(test_file)
    assert not test_file.exists()


def test_remove_directory(tmp_path: Path) -> None:
    """
    Test removing a directory.

    Args:
        tmp_path: Temporary directory path provided by pytest.

    Returns:
        None
    """

    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file.txt").write_text("test")
    assert test_dir.exists()

    remove(test_dir)
    assert not test_dir.exists()


def test_remove_nonexistent_path(tmp_path: Path) -> None:
    """
    Test removing a non-existent path does not raise error.

    Args:
        tmp_path: Temporary directory path provided by pytest.

    Returns:
        None
    """

    nonexistent = tmp_path / "nonexistent"
    remove(nonexistent)


@patch("hooks.post_gen_project.project_dir")
@patch("hooks.post_gen_project.remove")
def test_folder_removal_logic(mock_remove, mock_project_dir, tmp_path: Path) -> None:
    """
    Test that folders are removed when not enabled.

    Verifies the post-generation hook correctly removes optional
    folders based on cookiecutter configuration.

    Args:
        mock_remove: Mock of the remove function.
        mock_project_dir: Mock of the project directory path.
        tmp_path: Temporary directory path provided by pytest.

    Returns:
        None
    """
    
    mock_project_dir.__truediv__ = lambda self, x: tmp_path / x

    folders = {
        ".devcontainer": "no",
        ".vscode": "yes",
        "notebooks": "no",
        "prompts": "yes",
    }
    
    for folder, enabled in folders.items():
        if enabled != "yes":
            mock_remove(mock_project_dir / folder)

    assert mock_remove.call_count == 2
