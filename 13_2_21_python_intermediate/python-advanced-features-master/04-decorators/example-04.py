import functools


class Multiply:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self.multiplier

        return wrapper


@Multiply(2)
def double_addition(a, b):
    return a + b


@Multiply(3)
def triple_addition(a, b):
    return a + b


if __name__ == "__main__":
    print(double_addition(2, 2))
    print(triple_addition(1, 1))
