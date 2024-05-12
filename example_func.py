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
    Функция возведения числа в степень.
    :return: int
    """
    c = plus(2, 2)
    return c ** 2


if __name__ == '__main__':
    print(step())
