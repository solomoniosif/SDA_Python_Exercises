from copy import deepcopy

l1 = [1, 2, 3]

l2 = l1
l2.append(4)
l3 = deepcopy(l1)

l3.append(5)

print(l1)
print(l2)
print(l3)


def add_in_list(el, lst):
    lst.append(el)
    return lst


l4 = add_in_list(6, l1)

print(l1, l2, l3, l4)
