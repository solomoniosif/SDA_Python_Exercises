import functools
from time import perf_counter


def example_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper: Before function execution")
        result = func(*args, **kwargs)
        print("Wrapper: after function execution")
        return result

    return wrapper


def timer(func, runs=10000):
    _elapsed_time = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal _elapsed_time
        start = perf_counter()
        for _ in range(runs):
            result = func(*args, **kwargs)
        stop = perf_counter()
        _elapsed_time = stop - start
        return result

    def elapsed_time():
        return _elapsed_time

    wrapper.elapsed_time = elapsed_time
    return wrapper



@example_decorator
def greeting(name):
    print(f"Hello, {name}!")

greeting("Jane")

    
def power(x, y):
    return x ** y

power = timer(power, runs=1000000000000000000)

print(pow(2, 2))
print(power.elapsed_time())
