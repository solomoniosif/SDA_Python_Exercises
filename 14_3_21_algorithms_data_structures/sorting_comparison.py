from timer import time_execution
import random


@time_execution
def bubble_sort(lst):
    ordered = False
    while not ordered:
        in_order = []
        for i in range(len(lst) - 1):
            a, b = lst[i], lst[i + 1]
            if a > b:
                in_order.append(False)
                lst[i + 1] = a
                lst[i] = b
            else:
                in_order.append(True)
        ordered = all(in_order)
    return lst


@time_execution
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_el = lst[i]
        current_idx = i - 1
        while current_idx >= 0:
            if current_el < lst[current_idx]:
                lst[current_idx + 1] = lst[current_idx]
                lst[current_idx] = current_el
                current_idx = current_idx - 1
            else:
                break
    return lst


def merge(left, right):
    left_i = 0
    right_i = 0
    result = []
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    result.extend(left[left_i:])
    result.extend(right[right_i:])
    return result


def merge_sort(l):
    if len(l) < 2:
        return l
    middle = len(l) // 2
    sorted_left = merge_sort(l[:middle])
    sorted_right = merge_sort(l[middle:])
    return merge(sorted_left, sorted_right)


@time_execution
def merge_sort_time(l):
    return merge_sort(l)


if __name__ == '__main__':
    sample_list = list(range(10000, 1, -1))
    random.shuffle(sample_list)

    sample_list2 = list(range(7000))
    random.shuffle(sample_list2)

    bubble_sort(sample_list2)
    insertion_sort(sample_list)
    merge_sort_time(sample_list)
