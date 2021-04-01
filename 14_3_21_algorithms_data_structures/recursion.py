from timer import time_execution


# import sys
#
#
# sys.setrecursionlimit(10 ** 6)


@time_execution
def recursive_factorial(n):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    return factorial(n)


@time_execution
def iterative_factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


# print(f"5! = {recursive_factorial(777)}")
# print(f"5! = {iterative_factorial(777)}")


@time_execution
def recursive_fibonacci(n):
    def inner(n):
        if n in [0, 1]:
            return n
        return inner(n - 1) + inner(n - 2)

    return inner(n)


@time_execution
def iterative_fibonacci(n):
    i = 0
    b = 1
    a = 0

    while i < n:
        c = b + a
        b = a
        a = c
        i += 1
    return c


print(recursive_fibonacci(32))
print(iterative_fibonacci(32))
