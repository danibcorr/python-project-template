# 3pps
import pytest


@pytest.fixture(autouse=True)
def reset_modules():
    """
    Reset imported modules between tests.

    Ensures test isolation by clearing module state after each test.

    Returns:
        None
    """
    
    yield
