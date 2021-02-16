import random
import string
import functools

alphabet = string.ascii_letters + string.punctuation + string.digits


def lowercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()

    return wrapper


def shorten(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result if len(result) <= 40 else result[:40]

    return wrapper


@lowercase
@shorten
def random_string():
    length = random.randint(30, 60)
    population = []
    for _ in range(length):
        index = random.randint(0, len(alphabet) - 1)
        population.append(alphabet[index])
    return "".join(population)


if __name__ == "__main__":
    for _ in range(10):
        print(random_string())
