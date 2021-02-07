
# ! #########################################################################
# ! #################       POLYMORPHISM IN PYTHON       ####################
# ! #########################################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hours, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hours)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hours + self.scholarship


print(__name__)

if __name__ == '__main__':
    john = Employee('John', 47, 20, 160)
    eric = Student('Eric', 20, 900)
    michael = WorkingStudent('Michael', 23, 9, 70, 900)

    family = [john, eric, michael]

    for member in family:
        print(f"\n{member.name} has a total income of ${member.show_finance()} per month.")
        print(f"{member.name} is an instance of {member.__class__.__name__} class.")
    print()

    family.append(Person('Mary', 78))

    for member in family:
        print(member)
