import pytest


@pytest.mark.skip(reason="function deprecated")
def test_foo():
    assert foo() == 1


def get_from_db():
    return NotImplemented


@pytest.mark.xfail
def test_get_from_db():
    # Represents future expected behaviour
    result = get_from_db()
    assert isinstance(result, list)
