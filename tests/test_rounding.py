import pytest

from src.altermath import floor, ceil, trunc


# -----------------
# floor
# -----------------

@pytest.mark.parametrize(
    "nums, expected",
    [
        ((5,), 5),
        ((5.7,), 5),
        ((-5.7,), -6),
        ((-5,), -5),
        ((1.2, 2.8, -3.4), [1, 2, -4]),
    ],
)
def test_floor(nums, expected):
    assert floor(*nums) == expected


def test_floor_empty():
    assert floor() is None


# -----------------
# ceil
# -----------------

@pytest.mark.parametrize(
    "nums, expected",
    [
        ((5,), 5),
        ((5.2,), 6),
        ((-5.7,), -5),
        ((-5,), -5),
        ((1.2, 2.8, -3.4), [2, 3, -3]),
    ],
)
def test_ceil(nums, expected):
    assert ceil(*nums) == expected


def test_ceil_empty():
    assert ceil() is None


# -----------------
# trunc
# -----------------

@pytest.mark.parametrize(
    "nums, expected",
    [
        ((5,), 5),
        ((5.7,), 5),
        ((-5.7,), -5),
        ((-5,), -5),
        ((1.2, 2.8, -3.4), [1, 2, -3]),
    ],
)
def test_trunc(nums, expected):
    assert trunc(*nums) == expected


def test_trunc_empty():
    assert trunc() is None
