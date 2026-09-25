from src.altermath import square, cube, power


# -----------------
# square
# -----------------

def test_square_one_number():
    assert square(4) == 16


def test_square_multiple_numbers():
    assert square(2, 3, 4) == [4, 9, 16]


def test_square_empty():
    assert square() is None


def test_square_negative():
    assert square(-3) == 9 


# -----------------
# cube
# -----------------

def test_cube_one_number():
    assert cube(3) == 27


def test_cube_multiple_numbers():
    assert cube(2, 3) == [8, 27]


def test_cube_empty():
    assert cube() is None


def test_cube_negative():
    assert cube(-3) == -27 


# -----------------
# power
# -----------------

def test_power_one_number():
    assert power(2, exp=4) == 16


def test_power_multiple_numbers():
    assert power(2, 3, 4, exp=2) == [4, 9, 16]


def test_power_zero_exp():
    assert power(2, 5, exp=0) == [1, 1]


def test_power_empty():
    assert power(exp=2) is None


def test_power_negative():
    assert power(-3, exp=2) == 9


def test_power_negative_exp():
    assert power(100, exp=-1) == 0.01
