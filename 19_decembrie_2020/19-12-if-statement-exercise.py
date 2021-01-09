# 2. Inside that folder, create file if-statement-exercise.py.
# 3. Write an application that:
# a. Asks user for a number from 1 to 7.
# b. If the number provided by user is smaller than 1, prints out "There are no negative
# number days!".
# c. For input number 1, prints out "You chose Monday".
# d. If the number provided by user is greater than 7, prints out "There are only 7 days in a
# week!".


user_number = int(input("Enter a number from 1 to 7: "))

if user_number < 1:
    print("There are no negative number days!")
elif user_number == 1:
    print("You chose Monday")
elif user_number > 7:
    print("There are only 7 days in a week!")
