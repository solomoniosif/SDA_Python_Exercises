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
import functools
import logging


def decorate(func):
    def wrapper(*args, **kwargs):
        logging.info("INFO: calling a function")
        return func(*args, *kwargs)

    return wrapper


@decorate
def complex_calculation(a, b):
    logging.debug("DEBUG: performing complex calculation")
    result = a + b
    logging.debug(f"DEBUG: result={result}")
    return result



if __name__ == "__main__":
    l = logging.getLogger()
    l.setLevel(logging.DEBUG)

    # CONSOLE Handler
    console_handler = logging.StreamHandler() #`asctime [level]: message` level WARN
    console_handler.setLevel(logging.WARN)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    )
    l.addHandler(console_handler)

    # File A Handler
    file_handler_a = logging.FileHandler("file_a.log", mode="w+")
    file_handler_a.setLevel(logging.DEBUG)
    file_handler_a.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s") # File A: `timestamp - level - message` level DEBUG
    )
    l.addHandler(file_handler_a)

    # File B Handler
    file_handler_b = logging.FileHandler("file_b.log", mode="w+")
    file_handler_b.setLevel(logging.INFO)
    file_handler_b.setFormatter(
        logging.Formatter("%(filename)s - %(funcName)s - %(lineno)d") # `filename - funcname - line number` level INFO
    )
    l.addHandler(file_handler_b)


    for _ in range(10):
        result = complex_calculation(random.randint(0, 15), random.randint(0, 15))
        if result <= 10:
            logging.warning("WARN: a warning")
        elif result <= 20:
            logging.error("ERROR: an error")
        elif result <= 30:
            logging.critical("CRITICAL: a critical error")
