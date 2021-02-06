def greeting(name):
    return f"Hello, {name}"


def test_greeting():
    assert greeting("Kate") == "Hello, Kate"

