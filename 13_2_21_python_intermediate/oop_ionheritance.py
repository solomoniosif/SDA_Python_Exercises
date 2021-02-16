import playsound




class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_a_sound(self):
        return ""


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_a_sound(self):
        return 'Woof!'

    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_a_sound(self):
        return 'Meaw!'



if __name__ == '__main__':
    a = Animal('animal', 12)
    d = Dog('Rex', 7)
    c = Cat('Oli', 1)

    print(a.make_a_sound())
    print(d.make_a_sound())
    print(c.make_a_sound())