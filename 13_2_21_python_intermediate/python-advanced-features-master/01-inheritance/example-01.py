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
    fido = Dog("Fido")
    print(fido.name)
