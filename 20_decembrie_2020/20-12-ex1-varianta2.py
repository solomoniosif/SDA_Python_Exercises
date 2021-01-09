import sys

# The user enters two numbers separated by ",". 
# Print out if the first number is greater, less or equal to the second number.

numbers = sys.argv[1:]
num1, num2 = numbers[0].split(",")


if int(num1) > int(num2):
    print(f"{num1} is greater than {num2}")
elif int(num1) == int(num2):
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is less than {num2}")