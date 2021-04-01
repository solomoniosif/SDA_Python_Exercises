"""
A decorator class to time functions runtime
"""

import time


class TimerDecorator:
    """
    A class decorator for timing functions runtime
    """

    def __init__(self, func):
        self.times = []
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        delta_time = time.time() - start_time
        self.times.append(delta_time)
        print(
            f"Function {self.func.__name__} has been executed in {delta_time}s "
            f"with the following arguments: {args} {kwargs}"
        )
        return result

    def get_times(self):
        """
        Method to get times stored by the instance of the TimerDecorator class
        :return: list of runtimes of functions decorated with this
        """
        return self.times


@TimerDecorator
def calculate_product_a_million_times(small_number):
    """
    A function that makes a calculation with multiplication, power
    and addition a million times.
    :param small_number: int
    :return: None
    """
    for _ in range(1_000_000):
        large_number = 4 ** 39
        _ = large_number * small_number + small_number ** 39


if __name__ == "__main__":
    calculate_product_a_million_times(10)
