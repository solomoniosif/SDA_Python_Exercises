# Implementation of a linear search algorithm.


def linear_search(lst, lookup_value):
    for idx, el in enumerate(lst):
        if el == lookup_value:
            return f"'{lookup_value}' found at position {idx}"
    return f"'{lookup_value}' not found"


def linear_search2(lst, lookup_value):
    for i in range(len(lst)):
        if lst[i] == lookup_value:
            return f"'{lookup_value}' found at position {i}"
    return f"'{lookup_value}' not found"


def linear_search3(lst, lookup_value):
    for el in lst:
        if el == lookup_value:
            return f"'{lookup_value}' found at position {lst.index(el)}"
    return f"'{lookup_value}' not found"


sample_list = [4, 7, 3, 9, 8, 12, 1]
print(linear_search(sample_list, 12))
print(linear_search2(sample_list, 12))
print(linear_search3(sample_list, 12))
