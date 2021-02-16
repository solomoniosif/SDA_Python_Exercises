"""
1. Write a generator called `elements` which takes two arguments: generator
 `gen` and integer `max_elem`. `elements` should yield no more than 
 `max_elem` items from generator `gen`. We assume `gen` is always infinite 
 or longer than `max_elem`.
2. Use `elements` to get 50 first numbers in Fibonacci sequence from 
example-05.py
"""


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def elements(gen, max_elem):
    for _ in range(max_elem):
        yield next(gen)


if __name__ == "__main__":
    fib = fibonacci()

    for i, element in enumerate(elements(fib, 50)):
        print(f"fib({i}): {element}")
