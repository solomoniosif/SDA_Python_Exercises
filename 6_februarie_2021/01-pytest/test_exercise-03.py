from collections import Counter
import pytest

def is_anagram(word, other_word):
    """is_anagram checks whether other_word is an anagram of word"""
    if len(word) == 0 or len(other_word) == 0:
        return False
    return Counter(word) == Counter(other_word)

def is_anagram2(word, other_word):
    if len(word) == 0 or len(other_word) == 0:
        return False
    return sorted(word.lower().replace(' ', '')) == sorted(other_word.lower().replace(' ', ''))

def validate_coordinates(latitude, longitude):
    """validate_coordinates checks whether provided latitude and 
    longitude constitute a valid pair of GPS coordinates"""
    return -90.0 <= latitude <= 90 and -180.0 <= longitude <= 180.0


@pytest.mark.parametrize(
    "word, other_word, expected_result",
    [
        ('listen', 'silent', True),
        ('Listen', 'silent', False),
        ('12345', '54321', True),
        ('a gentelman', 'elegant man', True),
        ('elbow', 'below', True),
        ('dragnea', 'grenada', True),
        ('', '', False),
        ('School master', 'The classroom', False),
        ('Funeral', 'Real fun', False)
    ]
)
def test_is_anagram(word, other_word, expected_result):
    assert is_anagram(word, other_word) == expected_result


@pytest.mark.parametrize(
    "word, other_word, expected_result",
    [
        ('listen', 'silent', True),
        ('Listen', 'silent', True),
        ('12345', '54321', True),
        ('a gentelman', 'elegant man', True),
        ('Elbow', 'Below', True),
        ('dragnea', 'grenada', True),
        ('', '', False),
        ('School master', 'The classroom', True),
        ('Funeral', 'Real fun', True)
    ]
)
def test_is_anagram2(word, other_word, expected_result):
    assert is_anagram2(word, other_word) ==  expected_result


@pytest.mark.parametrize(
    "latitude, longitude, expected_result",
    [
        (45, 125, True),
        (-90, 180, True),
        (125, 45, False),
        (-91, -181, False)
    ]    
)
def test_validate_coordinates(latitude, longitude, expected_result):
    assert validate_coordinates(latitude, longitude) == expected_result
