from src.altermath import sqrt, root


# -----------------
# sqrt
# -----------------

def test_sqrt_multiple_numbers():
    assert sqrt(9, 36, 81) == [3, 6, 9]


def test_sqrt_one_number():
    assert sqrt(64) == 8


def test_sqrt_empty():
    assert sqrt() is None


def test_sqrt_zero():
    assert sqrt(0) == 0


def test_sqrt_negative():
    assert sqrt(-1) is None


def test_non_integer_sqrt():
    assert root(3, index=2) == 3 ** 0.5


# -----------------
# root
# -----------------

def test_root_multiple_numbers():
    assert root(27, 216, 729, index=3) == [3, 6, 9]


def test_root_one_number():
    assert root(64, index=2) == 8


def test_root_empty():
    assert root(index=2) is None


def test_root_zero():
    assert root(0, index=2) == 0


def test_root_negative_odd():
    assert root(-27, index=3) == -3


def test_root_negative_even():
    assert root(-16, index=2) is None


def test_root_index_less_than_two():
    assert root(16, index=1) is None


def test_float_index():
    assert root(16, index=2.5) is None


def test_non_integer_root():
    assert root(4, index=4) == 4 ** 0.25
