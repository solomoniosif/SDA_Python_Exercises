
# ! Accessing private class atributes through class methods

# class Animal:
#     def __init__(self, name='Rex', age=2):
#         self.__name = name
#         self.__age = age

#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be grather than 0.")

#     def get_age(self):
#         return self.__age


# ! Accessing private class atributes through property decorators (The pythonic way)

class Animal:
    def __init__(self, name, age):
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
            print("Age must be grather than 0")


my_dog = Animal('Rex', 5)

my_dog.age = 3