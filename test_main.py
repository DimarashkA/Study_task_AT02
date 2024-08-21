import pytest

from main import check

def test_check_1():
    assert check(4) == True

def test_check_2():
    assert check(3) == False

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (56, True),
    (0, True),
    (3, False),
    (-5, False)
])

def test_check_whith_param(number, expected):
    assert check(number) == expected
