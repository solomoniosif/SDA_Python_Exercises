# Print out a table with header row containing name, age and salary where each is accordingly
# extended to 15, 5 and 12 characters.
#  Print out a line to separate header from data columns that has precisely the table's length.
#  Print out 3 data rows in that table where all columns are even with header columns and salary
# has two digits after comma.
# | Name | Age | SalarĀ |
# ------------------------------------------
# | John Doe | 27 | 123456.00 |
# | John Wick | 40 | 50000.00 |
# | Jeff Bezos | 45 | 999999999.95 |


header_name = "Name"
header_age = "Age"
header_salary = "Salary"
header = f"| {header_name:15} | {header_age:5} | {header_salary:12}"

print(header)
print("-"*len(header))

name_1 = "John Doe"
age_1 = 27
salary_1 = 123456
print(f"| {name_1:15} | {age_1:5} | {salary_1:12.2f}")

name_2 = "John Wick"
age_2 = 40
salary_2 = 50000
print(f"| {name_2:15} | {age_2:5} | {salary_2:12.2f}")

name_3 = "Jeff Bezos"
age_3 = 45
salary_3 = 999999999.95
print(f"| {name_3:15} | {age_3:5} | {salary_3:12.2f}")
