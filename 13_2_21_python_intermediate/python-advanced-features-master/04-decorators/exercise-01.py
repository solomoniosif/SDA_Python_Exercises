import random
import string

alphabet = string.ascii_letters + string.punctuation + string.digits


def random_string():
    length = random.randint(30, 60)
    population = []
    for _ in range(length):
        index = random.randint(0, len(alphabet) - 1)
        population.append(alphabet[index])
    return "".join(population)
