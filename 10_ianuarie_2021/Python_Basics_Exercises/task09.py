# Write a program that retrieves an integer string from the user. Downloading data ends with the number 0 (not included in the data). 
# Then, the program calculates the sum of the largest and smallest of the given numbers and their arithmetic average 
# and prints them in the console.

# For example, for a series of given numbers: 1, -4, 2, 17, 0, the program should write in the console the numbers: 13, 6.5.   
# Get data from the user in the console using argument-less input().

numbers = []

while True:
    next_num = int(input())
    if next_num == 0:
        break
    else:
        numbers.append(next_num)

sum_largest_smallest = max(numbers) + min(numbers)
avg_largest_smallest = sum_largest_smallest / 2

print(sum_largest_smallest)
print(avg_largest_smallest)