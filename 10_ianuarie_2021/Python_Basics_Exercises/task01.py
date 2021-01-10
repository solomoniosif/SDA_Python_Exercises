# Write a program that, based on the variables: height - height (int) and weight - weight (float), 
# checks whether a person can ride a roller coaster.

# If the person is at least 150cm tall and does not exceed 180kg, the program will write in the console 
# 'Fasten seat belts!', Otherwise it will write in the console 'I'm sorry you can't ride!'.

# Get the data from the user in the console using argument-less input().

height = int(input())
weight = float(input())

if height >= 150 and weight <= 180:
    print("Fasten seat belts!")
else:
    print("I'm sorry you can't ride!")