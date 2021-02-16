from functools import wraps
import time


def timer(runs):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print("Starting calculation ...")
            start_time = time.time()
            for _ in range(runs):
                result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            return result
        return wrap
    return wrapper


@timer(10_000_000)
def power(x, y):
    x ** y

if __name__ == '__main__':
    power(15,15)