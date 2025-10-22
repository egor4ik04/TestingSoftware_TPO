import pytest
from calculator import Calculator

calc = Calculator()


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0),
    (2.5, 3.5, 6.0)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 0, 0),
    (2.5, 1.5, 1.0)
])
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 0, 0),
    (-1, 1, -1),
    (2.5, 4, 10.0)
])
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (5, 2, 2.5),
    (-10, 2, -5)
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (20, False),
    (1, False)
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, False),
    (1.5, False),
    (17, False),
    (-20, True),
    (0, True)
])
def test_is_even_number(n, expected):
    assert calc.is_even_number(n) == expected
    