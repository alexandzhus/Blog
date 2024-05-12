import pytest
from example_func import plus, step, two_num_multiplication


def test_plus():
    assert plus(10, 10) == 20


def test_plus_zero():
    assert plus(0, 0) == 0


def test_plus_must_be_zero_if_negative():
    assert plus(1, -1) == 0


def test_step():
    assert step() == 16


def test_two_num_multiplication():
    assert two_num_multiplication(3, 5) == 15


if __name__ == '__main__':
    pytest.main()
