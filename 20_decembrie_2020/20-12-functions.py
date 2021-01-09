
# ! Function without parameters   * * * * * * * * * * * * * * * * * * * *
def print_hello_world():
    print("Hello world!")

print_hello_world()

# ! Function with parameters      * * * * * * * * * * * * * * * * * * * *
def greet_by_name(name):
    print(f"Hello {name}!")

greet_by_name("Jack")

def print_full_name(name, surname):
    print(f"{name} {surname}")

print_full_name("Jack", "Bauer")

# ! Function with default parameters * * * * * * * * * * * * * * * * * * 
def greet_by_name2(name="World"):
    print(f"Hello {name}!")

greet_by_name2()
greet_by_name2("John")

# ! Function with return value    * * * * * * * * * * * * * * * * * * * *
def calculate_square(a):
    return a * a

square = calculate_square(5)
print(square)

# ! Function with an unknown number of arguments (*args) * * * * * * * * * 
def sum_of_numbers(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum_of_numbers(1,2,3,4,5))

# ! Function with an unknown number of key word arguments (*kwargs) * * * * 
def price_of_ingredients(**kwargs):
    result = 0
    for ingredient in kwargs:
        result += kwargs[ingredient]
    return result

recipe_cost = price_of_ingredients(water=0, flower=3, salt=0.5, sugar=3, eggs=4)
print(recipe_cost)

recipe2_cost = price_of_ingredients(flower=2, chocolate=5, cheese=7, cream=3, eggs=4)
print(recipe2_cost)


# ! Function with any number of non keyword and keyword arguments * * * * * 
def cheesecake_price(*args, **kwargs):
    result = 0
    for arg in args:
        result += 1
    for kwarg in kwargs:
        result += kwargs[kwarg]
    return result

classic_cheesecake = cheesecake_price(5, 2, 7, 8, flower=2, chocolate=5, cheese=7, cream=3, eggs=4)
print(classic_cheesecake)
