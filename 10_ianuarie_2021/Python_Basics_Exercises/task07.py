# Write a program that takes a positive integer N - n (int) from the user, 
# and then displays all powers of the number 2 in the console that are not greater than the number given.

# For example, for the number 71 the program should write in the console the numbers: 1 2 4 8 16 32 64.

# Get data from the user in the console using argument-less input().

n = int(input())

powers_of_2 = []
start_num = 1
while start_num <= n:
    powers_of_2.append(start_num)
    start_num *= 2

for num in powers_of_2:
    print(num)