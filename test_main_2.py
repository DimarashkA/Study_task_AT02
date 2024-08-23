import pytest
from main_2 import sort_list

def test_sort_1():
    assert sort_list([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_sort_2():
    assert sort_list([-3, 2, 0, -10]) == [-10, -3, 0, 2]

def test_sort_3():
    assert sort_list([]) == []
     