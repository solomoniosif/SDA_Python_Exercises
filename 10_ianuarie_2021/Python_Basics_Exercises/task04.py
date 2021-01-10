# Write a program which, based on the variables: amount - amount (float) and number of installments - number_of_installments (int), 
# will calculate the monthly loan installment and write it to the console. The parameters have restrictions:
# the loan amount must be between PLN 100.00 and PLN 10,000.00,
# the number of installments must be between 6 and 48.
# If the loan amount exceeds the acceptable range, the loan amount should be set at PLN 5,000.00. If the number of installments 
# exceeds the acceptable range, the number of installments should be set to 36.

# The calculated monthly installment should also include interest. To simplify the calculations, assume that you add X percent 
# to the loan amount depending on the number of installments:

# 6-12 installments - 2.5%,
# 13-24 installments - 5.0%,
# 25-48 installments - 10.0%,
# and then calculate the installment amount based on the number of installments.

# Get data from the user in the console using argument-less input().

amount = float(input())
number_of_instalments = int(input())

if amount < 100 or amount > 10000:
    amount = 5000

if number_of_instalments < 6 or number_of_instalments > 48:
    number_of_instalments = 36

interest = None
if number_of_instalments <= 12:
    interest = 0.025
elif number_of_instalments <= 24:
    interest = 0.05
elif number_of_instalments <= 48:
    interest = 0.1

total_amount = amount + (amount * interest)

monthly_loan = total_amount / number_of_instalments

print(monthly_loan)