from timer import time_execution


@time_execution
def naive_minimum(l):
    count = 0
    if len(l) == 0:
        return None
    minimum = float("inf")
    for elem in l:
        count = count + 1
        # print (elem)
        if elem < minimum:
            minimum = elem
    return minimum, count


if __name__ == "__main__":
    for elements in [100, 1000, 10_000]:
        print(f"For {elements} elements: ", end="")
        minim, count = naive_minimum(range(elements))
        print(minim, count)
