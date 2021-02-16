import random
from functools import wraps
from string import ascii_letters


def lower_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper

def shorten_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[:40]
    return wrapper

def title_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.title()
    return wrapper



@title_string
@lower_string
@shorten_string
def random_string():
    random_string = ""
    characters = ascii_letters + " . , ! ?"
    for _ in range(random.randint(7,70)):
        random_string += random.choice(characters)
    return random_string



if __name__ == "__main__":
    print("-".ljust(40, "-"))
    for _ in range(7):
        print(random_string())
    print("-".ljust(40, "-"))