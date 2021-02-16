def my_range(start, stop, step=1):
    position = start
    while position < stop:
        yield position
        position += step


def words():
    yield "This"
    yield "is"
    yield "a"
    yield "complete"
    yield "sentence"
    # calling next after this yield raises StopIteration


if __name__ == "__main__":
    r = my_range(100, 500, step=100)
    print(r)
    print([num for num in r])

    w = words()
    while True:
        print(next(w))
