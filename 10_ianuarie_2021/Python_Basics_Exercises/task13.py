# Write a program that reads the text entered by the user, and then:

# checks if the word "Python" appears in the text - if so, it prints the message "I found Python" in the console,
# checks if the text starts with the word "Python" - if so, it prints the message "Starts with Python" in the console,
# check if the text ends with the word "Python" - if so, it prints the message "Ends with Python" in the console,
# checks if the text equals the word "Python" - if so, prints the message "Equals Python" in the console,
# prints the index of the first occurrence of the word "Python" in the text in the console.
# For example, for the text "Python", the program should write in the console:

# I found Python
# Starts with Python
# Ends with Python
# Equals Python
# 0
# and for the text 'Python course from scratch is the best way to learn Python', the program should write in the console:

# I found Python
# Ends with Python
# 54
# Download data from the user in the console using argument-less input().

user_input = input()

if 'Python' in user_input:
    print("I found Python")

if user_input.startswith('Python'):
    print("Starts with Python")

if user_input.endswith('Python'):
    print("Ends with Python")

if user_input == 'Python':
    print("Equals Python")

print(user_input.index('Python'))
