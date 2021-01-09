
# ! Examples of FOR LOOPS

animals = ['dog', 'cat', 'horse']
for animal in animals:
    print(animal)

animal_string = 'elephant'
for ch in animal_string:
    print(ch)

fruits = ['apple', 'banana', 'orange', 'lemon']
for index, fruit in enumerate(fruits):
    print(f"Fruit no: {index} {fruit}.")

numbers = []
for i in range(1000):
    numbers.append(i)
print(len(numbers))


# ! LIST COMPREHENSION
numbers2 = [i for i in range(1000)]
print(len(numbers2))


# !  NESTED FOR LOOPS *
print(f".........................")
for animal in animals:
    for fruit in fruits:
        print(f"{animal} eats {fruit}.")
    print(f".........................")


# ! DICTIONARY COMPREHENSION 
word_lengths = {word:len(word) for word in animals}
print(word_lengths)

favourite_fruit = {animals[i]:fruits[i] for i in range(len(animals))}
print(favourite_fruit)