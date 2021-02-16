import functools

numbers = [1, 2, 3, 4, 5, 6]
sum_of_numbers = functools.reduce(lambda x, y: x + y, numbers)
print(f"Sum of {numbers} equals {sum_of_numbers}")

words = ["This", "is", "a", "list", "of", "words"]
print(functools.reduce(lambda x, y: f"{x} {y}", words))

minimum_of_numbers = functools.reduce(min, numbers, -3)
print(f"Found minimum is {minimum_of_numbers}")
