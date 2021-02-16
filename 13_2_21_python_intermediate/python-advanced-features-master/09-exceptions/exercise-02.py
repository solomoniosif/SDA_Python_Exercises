"""
Given function random_exception which raises a random exception every time,
write a try-except block which handles each of the possible exceptions by
counting their occurrences. Print the tally.
"""
import random

possible_exceptions = [OSError, IndexError, ZeroDivisionError]


def random_exception():
    raise random.choice(possible_exceptions)


if __name__ == "__main__":
    for _ in range(20):
        # handle exceptions thrown by random_exception here
        random_exception()
