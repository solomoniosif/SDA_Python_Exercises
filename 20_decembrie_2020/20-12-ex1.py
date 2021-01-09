# The user enters two numbers separated by ",". 
# Print out if the first number is greater, less or equal to the second number.


numbers = input("Enter two numbers separated by a comma: ")
num1, num2 = numbers.split(",")

if int(num1) > int(num2):
    print(f"{num1} is greater than {num2}")
elif int(num1) == int(num2):
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is less than {num2}")