# Standard libraries
import importlib
import sys
import unittest.mock as mock
from pathlib import Path

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


def test_folder_removal_logic(mock_project_dir: Path, tmp_path: Path) -> None:
    """
    Test that folders are removed when not enabled.

    Verifies the post-generation hook correctly removes optional
    folders based on cookiecutter configuration.

    Args:
        mock_project_dir: Mock project directory with optional folders.
        tmp_path: Temporary directory path provided by pytest.

    Returns:
        None
    """

    sys.modules.pop("hooks.post_gen_project", None)

    with mock.patch("pathlib.Path.cwd", return_value=mock_project_dir):
        # Own modules
        import hooks.post_gen_project as hook

        importlib.reload(hook)

    assert not (mock_project_dir / ".devcontainer").exists()
    assert not (mock_project_dir / ".vscode").exists()
    assert not (mock_project_dir / "notebooks").exists()
    assert not (mock_project_dir / "prompts").exists()
