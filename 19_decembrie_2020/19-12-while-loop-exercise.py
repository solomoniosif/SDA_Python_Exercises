# 2. Write an application that:
# a. Asks user for an input in a loop and prints it out.
# b. If the input is equal to "exit", program terminates printing out provided input and
# "Done.".
# c. If the input is equal to "exit-no-print", program terminates without printing out anything.
# d. If the input is equal to "no-print", program moves to next loop iteration without printing
# anything.
# e. If the input is different than "exit", "exit-no-print" and "no-print", program repeats.


# ? Varianta 1   * * * * * * * * * * * * * * * * 
while True:
    user_input = input("Enter an option: ")
    if user_input == "exit":
        print(user_input)
        print("Done.")
        break
    elif user_input == "exit-no-print":
        break
    elif user_input == "no-print":
        continue
    else:
        print(user_input)


# ? Varianta 2   * * * * * * * * * * * * * * * * 
# user_input = None
# while user_input != "exit":
#     user_input = input("Enter an option: ")
#     if user_input == "exit-no-print":
#         break
#     if user_input == "no-print":
#         continue
#     print(user_input)
# else:
#     print("Done.")
