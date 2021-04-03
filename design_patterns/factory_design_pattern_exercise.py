from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def test_drive(self):
        pass


class Volkswagen(Car):
    def __init__(self, model='Golf GTE', color='black'):
        self.model = model
        self.color = color

    def test_drive(self):
        print(f"A {self.color} Volkswagen {self.model} is ready for a test drive.")


class Audi(Car):
    def __init__(self, model='TT', color='red'):
        self.model = model
        self.color = color

    def test_drive(self):
        print(f"A {self.color} Audi {self.model} is ready for a test drive.")


class Mazda(Car):
    def __init__(self, model='3', color='white'):
        self.model = model
        self.color = color

    def test_drive(self):
        print(f"A {self.color} Mazda {self.model} is ready for a test drive.")


class Skoda(Car):
    def __init__(self, model='Superb', color='yellow'):
        self.model = model
        self.color = color

    def test_drive(self):
        print(f"A {self.color} Skoda {self.model} is ready for a test drive.")


# if __name__ == '__main__':
#     available_cars = {'vw': Volkswagen, 'audi': Audi, 'mazda': Mazda, 'skoda': Skoda}
# car_type = input('What car would you like to test? ')
#
# if car_type.lower() in available_cars:
#     car = available_cars[car_type.lower()]()
#     car.test_drive()
# else:
#     print(f"We currently don't have any {car_type.title()} "
#           f"available for a test drive.")


####################################
# Using a CarFactory
####################################

class CarFactory:
    _available_cars = {
            'vw': Volkswagen,
            'audi': Audi,
            'mazda': Mazda,
            'skoda': Skoda
    }

    @classmethod
    def build_car(cls, car_type):
        if car_type.lower() in cls._available_cars:
            return cls._available_cars[car_type.lower()]()
        else:
            print(f"We currently don't have any {car_type.title()} "
                  f"available for a test drive.")
            return None


if __name__ == '__main__':
    car_type = input('What car would you like to test? ')
    car = CarFactory.build_car(car_type)
    if car:
        car.test_drive()
