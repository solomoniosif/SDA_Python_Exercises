"""
1. Given list `digits = [1, 2, 5, 9]`, create a list of their squares
using `map()` and a lambda.
>>> digits = [1, 2, 5, 9]
>>> list(map(lambda x: x*x, digits))
[1, 4, 25, 81]

2. Given list `fruit = ["apples", "oranges", "grapes"]`, create a
dictionary, where the string is the key, and the value is string’s
length. Use `map()` and a lambda.
>>> fruit = ["apples", "oranges", "grapes"]
>>> dict(map(lambda s: (s, len(s)), fruit))
{'apples': 6, 'oranges': 7, 'grapes': 6}
"""
