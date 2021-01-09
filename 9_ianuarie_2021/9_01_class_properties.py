
class Animal():
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be grater than 0.")
    
    @age.deleter
    def age(self):
        del self.__age

    @property
    def name(self):
        return self.__name


my_dog = Animal("Max")

print(my_dog.age)
my_dog.age = 3
print(my_dog.age)

del my_dog.age

try:
    print(my_dog.age)
except:
    print(f"{my_dog.name} has no attribute 'age'.")
