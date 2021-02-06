import pytest


def test_expected_exception():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
