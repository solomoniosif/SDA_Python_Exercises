name = "Jedi"
title = "master"

# * FORMATTIING STRINGS IN PYTHON

#! Method 1: printf
print("Hello %s %s!" % (title, name))

#! Method 2: .format()
print("Hello {} {}!".format(title, name))

#! Method 3: f-string
print(f"Hello {title} {name}!")


header_name = "Name"
header_age = "Age"
header_salary = "Salary"
header = f"| {header_name:15} | {header_age:5} | {header_salary:12}"

print(header)
print("-"*len(header))

n = 109.234567891234
print(f"{n:.3f}")  # Will display only 3 decimals

percent = 0.72
print(f"{percent: .1%}")
