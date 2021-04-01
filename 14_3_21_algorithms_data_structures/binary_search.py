# Implementation of a binary search algorithm.


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


sample_lst = [1, 2, 3, 6, 8, 9, 12, 14, 23, 29, 33, 37, 39]

print(binary_search(sample_lst, 9))


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


l = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 45, 46, 47, 48, 49, 50]

print([l.index(x) for x in l])
print([binary_search2(l, x) for x in l])
