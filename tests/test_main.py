import pytest
from renovate_test.main import add_one, minus_one


def test_add_one_success():
    """Test sum function with two integers."""
    x: int = 10
    expected: int = 11
    actual: int = add_one(x)
    assert actual == expected


def test_add_one_exception():
    """Test sum function with two strings."""
    x: str = "10"
    with pytest.raises(TypeError):
        add_one(x)


def test_minus_one_succes():
    """Test sum function with two integers."""
    x: int = 10
    expected: int = 9
    actual: int = minus_one(x)
    assert actual == expected


def test_minus_one_exception():
    """Test sum function with two strings."""
    x: str = "10"
    with pytest.raises(TypeError):
        minus_one(x)
