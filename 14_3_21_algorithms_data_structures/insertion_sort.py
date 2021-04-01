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


sample_list = [5, 7, 9, 4, 2, 3, 6, 8, 1]

print(insertion_sort(sample_list))
