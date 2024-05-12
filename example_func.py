def plus(a: int, b: int) -> int:
    """
    Функция сложения двух целых чисел.

    :param a: int
    :param b: int
    :return: int
    """
    c = a + b
    return c


def step() -> int:
    """
    Функция возведения числа в степень. Используется другая функция plus.
    :return: int
    """
    c = plus(2, 2)
    return c ** 2


def two_num_multiplication(a: int, b: int) -> int:
    """
    Перемножение двух чисел.
    :param a: int
    :param b: int
    :return: int
    """
    return a * b


if __name__ == '__main__':
    print(step())
