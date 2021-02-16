class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f"My name is {self._name}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return f"My name is {self._name}, the dog."


if __name__ == "__main__":
    print(f"Dog is a subclass of Animal: {issubclass(Dog, Animal)}")
    print(f"Animal is a subclass of object: {issubclass(Animal, object)}")
    d = Dog("Rex")
    print(f"d is an instance of Dog: {isinstance(d, Dog)}")
    print(f"d is an instance of Animal: {isinstance(d, Animal)}")
    print(f"d is an instance of object: {isinstance(d, object)}")
