
# ? Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# * Expected Output : 0 1 2 4 5 

# ! Rezolvarea 1
for num in range(0, 7):
    if num not in [3,6]:
        print(num)

# ! Rezolvarea 2
for num in range(0, 7):
    if num != 3 and num != 6:
        print(num)
