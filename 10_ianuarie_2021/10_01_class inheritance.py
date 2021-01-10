class Bat():
    def eat(self, something):
        return f"Bat eats {something}"


class Man():
    def eat(self, something):
        return f"Man eats {something}"

    def work(self, at):
        return f"Man works at {at}"

    
class BatMan(Bat, Man):
    def __init__(self, name):
        self.name = name



a = BatMan("John")

print(a.eat('apples'))