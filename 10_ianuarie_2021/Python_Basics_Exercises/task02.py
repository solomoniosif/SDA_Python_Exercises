# Write a program that based on the variable temperature in degrees Celsius - temp_in_Celsius (float), 
# will calculate the temperature in degrees Farhenheit (degrees Fahrenheit = 1.8 * degrees Celsius + 32.0) 
# and write it in the console.

# Get the temperature from the user in the console using argument-less input().

temp_in_Celsius = float(input())

temp_in_Fahrenheit = 1.8 * temp_in_Celsius + 32
print(temp_in_Fahrenheit)