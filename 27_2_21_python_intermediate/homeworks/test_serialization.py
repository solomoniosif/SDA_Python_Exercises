import pytest
from serialization import average


def test_average_func():
    lst = [3, 5, 7]
    expected = 5.0
    assert average(lst) == expected


def test_only_numbers_counted():
    lst = [3, 5.0, 7, 'a']
    expected = 5.0
    assert average(lst) == expected

def test_empty_list():
    lst = []
    expected = None
    assert average(lst) == expected