import functools
import time
import math


class MeasureTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        delta_time = time.time() - start_time
        print(f"Function took {delta_time:.3f}s")
        return result


@MeasureTime
def power(x, y):
    for _ in range(1_000_000):
        result = math.pow(x, y)
    return result


if __name__ == "__main__":
    print(power(15.0, 60.0))
