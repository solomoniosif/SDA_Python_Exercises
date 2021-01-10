# Write a program that takes from the user two integers A - a (int) and B - b (int), where A < B, 
# and then calculates the sum of the sequence of numbers from A to B (A, A + 1, A + 2, ..., B) 
# and prints it in the console. 
# When the A < B condition is not met, the program exits by writing Job finished in the console.

# For example, for A = 4 and B = 11, the program should write the number 60 in the console.

# Get data from the user in the console using argument-less input().

a = int(input())
b = int(input())

if a < b:
    print(sum([num for num in range(a, b+1)]))
else:
    print("Job finished")