
# ? Write a Python program which iterates the integers from 1 to 50. 
# ? For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# ? For numbers which are multiples of both three and five print "FizzBuzz".
# * Sample Output : 
# * fizzbuzz
# * 1
# * 2
# * fizz
# * 4 
# * buzz


for num in range(1,50+1):
    if num % 3 == 0 and num % 5 == 0: # sau num % 15 == 0
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)