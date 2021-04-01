
generator_1 = (n ** 3 for n in range(1, 20) if n % 2 == 0)

list_1 = [num for num in generator_1]
print(list_1)

dict_1 = {num: pos for pos, num in enumerate(list_1)}

print(dict_1)


