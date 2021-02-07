
# ! #########################################################################
# ! #################       CLASS & STATIC METHODS       ####################
# ! #########################################################################

from oop_polymorphism import Person


class Student(Person):
    def __init__(self, name, age, scholarship):
        self.name = name
        self.age = age
        self.scholarship = scholarship

    
    def show_finance(self):
        return self.scholarship

    @classmethod
    def create_from_string(cls, sentence):
        name, age, scholarship = sentence.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 3:
            return True
        return False

if __name__ == '__main__':
    # * The @classmethod takes as the first parameter the class (cls). 
    # * To access a @classmethod from outside the class you cannot use the cls parameter, 
    # * you have to provide the name of the class
    student1 = Student.create_from_string("Iosif 33 900")
    print(student1)

    # * A @staticmethod neither takes a self or a cls parameter
    #  * To access it from outside the class you can do it either via the class or via the instance 
    print(Student.is_name_correct('iosif'))
    print(student1.is_name_correct('eric'))

    # * Instance methods require an object of its class to be created before it can be called
    student2 = Student('Eric', 21, 900)
    print(student2.show_finance())
    print(Student.show_finance(student1))
