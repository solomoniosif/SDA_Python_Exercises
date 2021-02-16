fruit = ["apple", "banana", "orange"]
fruit_iterator = iter(fruit)  # since lists are iterables, this returns an iterator
for f in fruit_iterator:
    print(f)
