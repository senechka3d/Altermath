import pytest

from src.altermath import add, subtract, multiply, divide, mod, fdiv, factorial


# -----------------
# add
# -----------------

def test_add_multiple_numbers():
    assert add(1, 2, 3) == 6


def test_add_one_number():
    assert add(5) == 5


def test_add_empty():
    assert add() is None


# -----------------
# subtract
# -----------------

def test_subtract_multiple_numbers():
    assert subtract(10, 3, 2) == 5


def test_subtract_one_number():
    assert subtract(7) == 7


def test_subtract_empty():
    assert subtract() is None


# -----------------
# multiply
# -----------------

def test_multiply_multiple_numbers():
    assert multiply(2, 3, 4) == 24


def test_multiply_one_number():
    assert multiply(5) == 5


def test_multiply_empty():
    assert multiply() is None


# -----------------
# divide
# -----------------

def test_divide_multiple_numbers():
    assert divide(20, 2, 2) == 5


def test_divide_float_result():
    assert divide(5, 2) == 2.5


def test_divide_integer_float_result():
    assert divide(8, 2) == 4


def test_divide_one_number():
    assert divide(10) == 10


def test_divide_empty():
    assert divide() is None


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# -----------------
# mod
# -----------------

def test_mod_multiple_numbers():
    assert mod(20, 6, 2) == 0


def test_mod_one_number():
    assert mod(7) == 7


def test_mod_empty():
    assert mod() is None


def test_mod_by_zero():
    with pytest.raises(ZeroDivisionError):
        mod(10, 0)


# -----------------
# fdiv
# -----------------

def test_fdiv_multiple_numbers():
    assert fdiv(20, 3) == 6


def test_fdiv_chain():
    assert fdiv(20, 3, 2) == 3


def test_fdiv_one_number():
    assert fdiv(10) == 10


def test_fdiv_empty():
    assert fdiv() is None


def test_fdiv_by_zero():
    with pytest.raises(ZeroDivisionError):
        fdiv(10, 0)


# -----------------
# factorial
# -----------------

def test_factorial_multiple_numbers():
    assert factorial(3, 5, 7) == [6, 120, 5040]


def test_factorial_one_number():
    assert factorial(6) == 720


def test_factorial_float():
    assert factorial(2.5) == None


def test_factorial_negative():
    assert factorial(-1) == None


def test_factorial_empty():
    assert factorial() == None
