"""
Given file exercise-01.py
    1. Convert all calls to `print()` to proper logging
    2. configure logging to log simultaneously to two files and console, using the following formats and levels:
        1. File A: `timestamp - level - message` level DEBUG
        2. File B: `filename - funcname - line number` level INFO
        3. Console: `asctime [level]: message` level WARN
"""

import time
import random
import logging
import functools


def decorate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("calling a function")
        return func(*args, *kwargs)

    return wrapper


@decorate
def complex_calculation(a, b):
    logging.debug("performing complex calculation")
    result = a + b
    logging.debug(f"result={result}")
    return result


if __name__ == "__main__":
    l = logging.getLogger()
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    )
    console_handler.setLevel(logging.WARN)
    l.addHandler(console_handler)

    fileA = logging.FileHandler("exercise-01-A.log")
    fileA.setFormatter(logging.Formatter("%(created)s - %(levelname)s - %(message)s"))
    fileA.setLevel(logging.DEBUG)
    l.addHandler(fileA)

    fileB = logging.FileHandler("exercise-01-B.log")
    fileB.setFormatter(logging.Formatter("%(filename)s - %(funcName)s - %(lineno)d"))
    fileB.setLevel(logging.INFO)
    l.addHandler(fileB)

    for _ in range(10):
        result = complex_calculation(random.randint(0, 15), random.randint(0, 15))
        if result <= 10:
            logging.warning("a warning")
        elif result <= 20:
            logging.error("an error")
        elif result <= 30:
            logging.critical("a critical error")
