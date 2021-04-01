from timer import time_execution
import random


@time_execution
def binary_search(lst, lookup_value):
    l, r = 0, len(lst)
    while True:
        half_idx = int((r + l) // 2)
        if lst[half_idx] == lookup_value:
            return f"'{lookup_value}' found at index {half_idx}"
        elif (r - l) <= 1:
            return f"'{lookup_value}' not found"
        elif lst[half_idx] < lookup_value:
            l = half_idx
        elif lst[half_idx] > lookup_value:
            r = half_idx


@time_execution
def binary_search2(lista, x):
    mid = len(lista) // 2
    add = 0
    while len(lista) > 0:
        if x == lista[mid]:
            return mid + add
        if x > lista[mid]:
            lista = lista[mid:]
            add = add + mid
        else:
            lista = lista[:mid]  # x < lista [mid]
        mid = len(lista) // 2
    return False


@time_execution
def linear_search(l, x):
    for el in l:
        if el == x:
            return True
    return False


if __name__ == '__main__':
    sample_list = list(range(80_000_000))
    x = random.choice(sample_list)

    print(binary_search(sample_list, x))
    print(binary_search2(sample_list, x))
    print(linear_search(sample_list, x))
