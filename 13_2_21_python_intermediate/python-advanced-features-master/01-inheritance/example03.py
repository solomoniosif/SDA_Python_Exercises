class A:
    def __init__(self):
        print(f"A init called")


class B(A):
    def __init__(self):
        super().__init__()
        print(f"B init called")


class C(B):
    def __init__(self):
        super().__init__()
        print(f"C init called")


class D(A):
    def __init__(self):
        super().__init__()
        print(f"D init called")


if __name__ == "__main__":
    print("Creating an instance of class C")
    c = C()
    print("Creating an instance of class D")
    d = D()
