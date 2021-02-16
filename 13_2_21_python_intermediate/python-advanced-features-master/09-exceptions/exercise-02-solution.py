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
    count = {e_type: 0 for e_type in possible_exceptions}

    for _ in range(20):
        try:
            random_exception()
        except OSError:
            count[OSError] += 1
        except IndexError:
            count[IndexError] += 1
        except ZeroDivisionError:
            count[ZeroDivisionError] += 1

    print(count)
