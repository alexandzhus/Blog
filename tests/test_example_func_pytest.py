import pytest
from example_func import plus, step, two_num_multiplication


def test_plus():
    
    """
    Описание теста
    """
    assert plus(10, 10) == 30


def test_plus_zero():
    assert plus(0, 0) == 0


def test_plus_must_be_zero_if_negative():
    assert plus(1, -1) == 0


def test_step():
    assert step() == 16


def test_two_num_multiplication():
    assert two_num_multiplication(3, 5) == 15

def test_step_for_null():
    assert step() == 0


if __name__ == '__main__':
    pytest.main()
