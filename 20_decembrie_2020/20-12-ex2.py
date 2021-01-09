
# ? Write a while loop which will print out all the even numbers between 0(inclusively)  
# ? and a number introduced by the user

# ! Varianta 1 - cu while loop  * * * * * * * * * *

user_number = int(input("Enter a number: "))
current_number = 0
while current_number <= user_number:
    if current_number % 2 == 0:
        print(current_number)
    current_number += 1

 
# ! Varianta 2 - cu for loop  * * * * * * * * * * *

for number in range(0, user_number+1):
    if number % 2 == 0:
        print(number)