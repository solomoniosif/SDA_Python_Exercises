def test_greeen():
    assert 1 > 0


def test_identity_fail():
    assert True is True


def test_exception_fail():
    assert 1 / 0.1
