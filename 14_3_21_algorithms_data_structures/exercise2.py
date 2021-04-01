from timer import time_execution


@time_execution
def quadratic_function(l):
    for el in l:
        for el2 in l:
            el * el2
    return True


if __name__ == "__main__":
    for elements in [100, 1000, 2_000,  5_000, 10_000]:
        print(f"For {elements} elements: ", end="")
        print(quadratic_function(range(elements)))

