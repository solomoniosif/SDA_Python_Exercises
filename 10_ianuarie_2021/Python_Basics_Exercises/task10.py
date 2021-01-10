# Write a program that takes an integer from the user and prints all its divisors in the console.

# For example, for the number 21, the program should write in the console the numbers: 1, 3, 7, 21   
# Get data from the user in the console using argument-less input().

num = int(input())

for n in range(1, num+1):
    if num % n == 0:
        print(n)