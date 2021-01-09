
class Human():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height ** 2)


class Programmer(Human):
    def __init__(self, name, height, weight, languages):
        super().__init__(name, height, weight)
        self.languages = languages

bob = Programmer("Bob", 180, 93, ["Python", "Java", "Go"])

print(bob.name)
print(f"{bob.name} has a BMI of {bob.bmi} and knows the following programming languages: {', '.join(bob.languages)}.")
