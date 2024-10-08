import pytest
from main_1 import is_palindrome


def test_is_palindrome_true():
    assert is_palindrome('madam') == True

def test_is_palindrome_false():
    assert is_palindrome('hello') == False

@pytest.mark.parametrize('test_input, expected', [
    ('racecar', True),
    ('hello', False),
    ('12321', True),
    ('', True),
    ('a', True),
    ('abba', True),
    ('level', True),
    ('level!', False),
    ('level?', False),
    ('level!!', False),
    ('', True),
])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
    