fruit = ["apple", "banana", "orange"]
fruit_iterator = iter(fruit)  # since lists are iterables, this returns an iterator
print(fruit_iterator)

print(next(fruit_iterator))
print(next(fruit_iterator))
print(fruit_iterator.__next__())
print(next(fruit_iterator))
