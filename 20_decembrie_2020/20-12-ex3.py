# Write a Python program to construct the following pattern, using a for loop.
# * 
# * * 
# * * * 
# * * * * 

height = int(input("Enter a number: "))

for i in range(1, height+1, 1):
    print(i*'* ')


for i in range(height+1, 0, -1):
    print(i*'* ')