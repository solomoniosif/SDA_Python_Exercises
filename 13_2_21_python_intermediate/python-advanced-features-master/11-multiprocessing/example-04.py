import random
import multiprocessing


def complex_calculation(a, b, c):
    return a ** b % c


if __name__ == "__main__":
    argument_lists = [
        (random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))
        for _ in range(500)
    ]

    with multiprocessing.Pool(10) as workers:
        result = workers.starmap(complex_calculation, argument_lists)

    for i in range(5):
        print(f"{argument_lists[i]} -> {result[i]}")
    print("...")
