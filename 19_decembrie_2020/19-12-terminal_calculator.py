import sys

first_number = sys.argv[1]
operation = sys.argv[2]
second_number = sys.argv[3]
result = eval(f"{first_number}{operation}{second_number}")

print(f"{first_number} {operation} {second_number} = {result}")