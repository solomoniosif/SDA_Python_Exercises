
digits = [1, 2, 5, 9]

squared_digits = list(map(lambda x: x**2, digits))

print(digits)
print(squared_digits)


fruits = ['apples', 'oranges', 'grapes']

fruit_dict = dict(map(lambda fruit: (fruit, len(fruit)), fruits))

print(fruit_dict)

for fruit in fruit_dict:
    print(fruit)