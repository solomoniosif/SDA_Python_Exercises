import pytest


def is_palindrome(word):
    if len(word) == 0:
        return False
    return word == word[::-1]


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("", False),
        ('ana', True), 
        ('banana', False),
        ('Ana', False)
    ],
)
def test_palindrome_check(word, expected_result):
    assert is_palindrome(word) is expected_result
