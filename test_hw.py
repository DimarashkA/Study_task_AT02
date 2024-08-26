import pytest
from homework import count_vowels

def test_vowels_only_english():
    assert count_vowels("aeiouAEIOU") == 10

def test_vowels_only_russian():
    assert count_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == 20

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("бгджз") == 0

def test_mixed_case_english():
    assert count_vowels("Hello World!") == 3

def test_mixed_case_russian():
    assert count_vowels("Привет Мир!") == 3

def test_single_vowel_english():
    assert count_vowels("a") == 1
    assert count_vowels("b") == 0

def test_single_vowel_russian():
    assert count_vowels("а") == 1
    assert count_vowels("б") == 0

def test_empty_string():
    assert count_vowels("") == 0

if __name__ == "__main__":
    pytest.main()