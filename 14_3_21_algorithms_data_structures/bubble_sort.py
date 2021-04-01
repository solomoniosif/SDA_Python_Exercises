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


sample_list = [5, 7, 9, 4, 2, 3, 6, 8, 1]

print(bubble_sort(sample_list))
