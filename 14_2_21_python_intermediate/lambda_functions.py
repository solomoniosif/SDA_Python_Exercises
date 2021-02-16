
fruit = ['apples', 'bananas', 'oranges']
capitalized_fruit = list(map( lambda s: s.capitalize(), fruit))

print(fruit)
print(capitalized_fruit)

def capitalize(s):
    return s.capitalize()

capitalized_fruit2 = list(map(capitalize, fruit))

print(capitalized_fruit2)