# Write a program that takes a positive integer from the user - number (int), and then prints all positive odd numbers 
# not greater than the given number in the console in order.

# For example, for the number 15, the program should write in the console the numbers: 1, 3, 5, 7, 9, 11, 13, 15.

# Get data from the user in the console using argument-less input().

number = int(input())

for num in range(1, number+1):
    if num % 2 == 1:
        print(num)