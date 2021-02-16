class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return f"My name is {self._name}"

    @property
    def age(self):
        return f"I'm {self._age} years old!"

    def make_a_sound(self):
        return ""


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"My name is {self._name}, the dog."

    def make_a_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"My name is {self._name}, the cat."

    def make_a_sound(self):
        return "Meow!"
