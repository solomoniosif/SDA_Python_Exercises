import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)-8s (%(asctime)s): %(message)s"))
logger.addHandler(console_handler)


def divide_by_list(num, lst):
    for el in lst:
        if el != 0:
            result = num / el
            print(f"{num} / {el} = {result}")


divide_by_list(3, [1, 0, 2])


def divide_by_list2(num, lst):
    for el in lst:
        try:
            result = num / el
        except ZeroDivisionError:
            continue
        print(f"{num} / {el} = {result}")


divide_by_list2(2, [1, 0, 2])
