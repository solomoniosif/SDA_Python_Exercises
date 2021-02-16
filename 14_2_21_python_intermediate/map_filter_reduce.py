from functools import reduce


class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price


cars = [
    Car("Ford", "Anglia", 300.0),
    Car("Ford", "Cortina", 700.0),
    Car("Alfa Romeo", "Stradale 33", 190.0),
    Car("Alfa Romeo", "Giulia", 500.0),
    Car("Citroën", "2CV", 75.0),
    Car("Citroën", "Dyane", 105.0),
]

cheapest_citroen = reduce(min, map(lambda car: car.price, filter(lambda car: car.make == "Citroën", cars)))

citroëns = filter(lambda car: car.make == "Citroën", cars)
citroëns_prices = map(lambda car: car.price, citroëns)
cheapest_citroën = reduce(min, citroëns_prices)

print(cheapest_citroën)

total_cost_of_alfaromeo = reduce(lambda x, y: x + y, map(lambda car: car.price, filter(lambda car: car.make == "Alfa Romeo", cars)))

print(total_cost_of_alfaromeo)

number_of_fords = reduce(lambda x,y: x + y, map(lambda car: 1, filter(lambda car: car.make == "Ford", cars)))

print(number_of_fords)