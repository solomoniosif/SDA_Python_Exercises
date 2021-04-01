class Singleton:
    _instance = None

    def __init__(self, name='S1'):
        print(f"- Instance initialization: name={name}")
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("- Create a new instance")
            cls._instance = object.__new__(cls)
        print("- Returning existing instance")
        return cls._instance


if __name__ == "__main__":
    print(' *' * 20)
    s1 = Singleton()
    print(' *' * 20)
    s2 = Singleton()
    print(' *' * 20)
    print(id(s1) == id(s2))
    print(' *' * 20)
    s2.name = 'new Singleton name'
    print(s1.name)
