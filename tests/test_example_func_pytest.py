import pytest
from example_func import plus, step


def test_plus():
    assert plus(10, 10) == 20


def test_plus_zero():
    assert plus(0, 0) == 0


def test_plus_must_be_zero_if_negative():
    assert plus(1, -1) == 0


def test_step():
    c = plus(2, 2)
    assert c ** 2 == 16


if __name__ == '__main__':
    pytest.main()
