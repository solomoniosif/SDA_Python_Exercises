import math


def power(x, y):
    for _ in range(1_000_000):
        result = math.pow(x, y)
    return result
