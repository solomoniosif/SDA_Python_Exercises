import pytest

def shorten(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + '...'
    else:
        return text


@pytest.mark.parametrize(
    "text, max_length, expected_result",
    [
        ('Acesta este un simplu text', 10, 'Acesta ...'),
        ('Iosif Solomon', 13, 'Iosif Solomon')
    ]
)
def test_shorten(text, max_length, expected_result):
    assert shorten(text, max_length) == expected_result
