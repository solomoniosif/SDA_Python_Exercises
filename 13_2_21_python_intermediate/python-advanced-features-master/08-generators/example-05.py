def fibonacci():
    """This generator returns consecutive items in Fibonacci sequence.
    Fibonacci sequence is infinite: its first element equals 0, the 
    second equals 1, and every following element equals the sum of 
    two previous elements:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # Since Fibonacci sequence is infinite, we will print first 10 elements

    for i, element in enumerate(fibonacci()):
        if i > 10:  # this is crucial, otherwise the program runs forever
            break
        print(f"fib({i}): {element}")
