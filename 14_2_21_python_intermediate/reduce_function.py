from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
sum_of_numbers2 = sum(numbers)

print(sum_of_numbers, sum_of_numbers2)