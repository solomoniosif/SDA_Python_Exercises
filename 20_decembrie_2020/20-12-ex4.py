
# ? Write a Python program to count the number of even and odd numbers from a series of numbers. 
# * Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# * Expected Output : 
# * Number of even numbers : 5
# * Number of odd numbers : 4

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# ! Varianta 1 - cu for loop 
evens = 0
odds = 0
for num in numbers:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

# ! Varianta 2 - cu list comprehension
evens = len([num for num in numbers if num % 2 == 0])
odds = len([num for num in numbers if num % 2 != 0])

print(f"Number of even numbers: {evens}")
print(f"Number of odd numbers: {odds}")



# ? Count how many times a number appears in a list
numbers2 = [1,1,2,2,2,4]

# ! * Rezolvare 1
numbers_count = {}
for num in numbers2:
    if numbers_count.get(num) is None:
        numbers_count[num] = 1
    else:
        numbers_count[num] += 1
for num, count in numbers_count.items():
    print(f"The number {num} appears {count} in our list")


# ! Rezolvare 2
numbers_count2 = {}
for num in numbers2:
    numbers_count2[num] = numbers2.count(num)
for num, count in numbers_count2.items():
    print(f"The number {num} appears {count} in our list")



# ? Write a Python program to count the number of unique even and odd numbers from a series of numbers. 
numbers3 = [1,1,2,2,2,4]

# ! Rezolvare 1 - prin eliminarea duplicate din lista prin transformarea ei intr-un set
evens = 0
odds = 0
for num in set(numbers3):
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1
print(f"Number of unique even numbers: {evens}")
print(f"Number of unique odd numbers: {odds}")


# ! Rezolvare 2
evens2 = 0
odds2 = 0
new_numbers3 = []
for num in numbers3:
    if num % 2 == 0 and num not in new_numbers3:
        evens2 += 1
    elif num % 2 != 0 and num not in new_numbers3:
        odds2 += 1
    new_numbers3.append(num)
print(f"Number of unique even numbers: {evens2}")
print(f"Number of unique odd numbers: {odds2}")



