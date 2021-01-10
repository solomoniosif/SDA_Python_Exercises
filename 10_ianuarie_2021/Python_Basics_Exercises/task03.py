# Write a program which, based on the variable income of the float type, calculates the amount of personal income tax due 
# and writes it to the console.

# The tax is calculated according to the following rules:

# up to €85,528.00 tax is 18% of the base minus €556.02,
# from €85,528.00 tax is €14,839.02 + 32% of the surplus over €85,528.00,
# tax cannot be negative.
# Receive the revenue from the user in the console using argument-less input() and store it in the income variable.

income = float(input())

if income < 85528:
    tax = income * 0.18 - 556.02
    if tax < 0:
        tax = 0
else:
    tax = 14839.02 + (income - 85528) * 0.32

print(tax)