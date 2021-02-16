class Singleton:
    _instance = None

    def __init__(self, name):
        print(f"- Instance initialization: name={name}")
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("- Creating new instance")
            cls._instance = object.__new__(cls)
        print("- Returning existing instance")
        return cls._instance


if __name__ == "__main__":
    print("A ".ljust(30, "-"))
    s = Singleton("A")
    print(id(s))
    print("B ".ljust(30, "-"))
    s2 = Singleton("B")
    print(id(s2))
    print("C ".ljust(30, "-"))
    s3 = Singleton("C")

    print(f"They are all the same object: {s is s2 is s3}")
    print(f"Singleton._instance.name: {Singleton._instance.name}")
