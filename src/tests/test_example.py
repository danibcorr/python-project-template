import pytest

from src.utils.utils import print_name


@pytest.mark.parametrize("name", ["Example"])
def test_print_name(name, capsys):
    # Call the function with the provided name
    print_name(name=name)

    # Capture the output of the print statement
    captured = capsys.readouterr()

    # Check if the output matches the expected format
    assert captured.out == f"Hello {name}!\n"
