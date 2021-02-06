import pytest

# executed before tests
@pytest.fixture
def input_value():
    print("I'm executed before each test")
    return 12


def test_divisible_by_3(input_value):
    assert input_value % 2 == 0


def test_divisible_by_6(input_value):
    assert input_value % 3 == 0
