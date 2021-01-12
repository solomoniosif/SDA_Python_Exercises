# Write a program that counts how many times each of the numbers has appeared in the prepared table
# and prints a summary in the console. An array can contain ** only ** numbers from 1 to 10.

# For example, for the table `[6 5 4 5 10 5 8 3 10 6 6 6 4 3 2 8 1 3 4 7] ', the program
# should write in the console the number of occurrences of each number:

# 1 - 1
# 2 - 1
# 3 - 3
# 4 - 3
# 5 - 3
# 6 - 4
# 7 - 1
# 8 - 2
# 9 - 0
# 10 - 2
# An array containing numbers is prepared as the variable numbers.


def program(numbers):
    numbers_count = {}
    for num in range(1, 11):
        numbers_count[num] = numbers.count(num)
    for num in numbers_count:
        print(f"{num} - {numbers_count[num]}")


# Do not change code below this line
data = list()
amount = int(input())
for i in range(amount):
    data.append(int(input()))

program(data)
