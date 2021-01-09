
# ? Write a function max_of_three(a, b, c) which returns the biggest of the three numbers. 
# ? Then print the result calling the function


# ! Rezolvarea 1 - folosind functia max()
def max_of_three(a, b, c):
    return max(a,b,c)

print(max_of_three(-2, 2, 3))

# ! Rezolvarea 2 - folosinf if statement
def max_of_three2(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
print(max_of_three2(-2, 2, 3))

# ! Rezolvarea 3 - folosind un for loop
def max_of_three3(a, b, c):
    max_num = 0
    for num in [a,b,c]:
        if num > max_num:
            max_num = num
    return max_num

print(max_of_three3(-2, 2, 3))


# * Aceiasi functie facuta sa functioneze cu orice numar de argumente
# ! Varinata 1 
def get_max(*args):
    return max(args)
print(get_max(-2, 2, 3, 5, 9, 10))

# ! Varianta 2
def get_max2(*args):
    max_num = args[0]
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num

print(get_max2(-2, 2, 3, 55, 12, 32, -54, 29))