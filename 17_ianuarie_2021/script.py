import platform

platform_name = platform.system()

s = f"Hello world from {platform_name}!"

class Test:
    def __init__(self):
        self.a = 1

    def __str__(self):
        return "Clasa mea Test"

a = Test()

if __name__ == "__main__":
    print(s)
    print(a)
