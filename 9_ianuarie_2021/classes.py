
class Animal:
    NAME = ""
    AGE = 0

    def __init__(self):
        self.name = "John"
        self.age = 2

    def print_details(self):
        print(f"Name: {self.name}, age: {self.age}.")


    
john = Animal()

print(john.name)
print(john.age)
