"""Given car list from example-04, find out the following using reduce-filter or map-filter-reduce:

1. What is the total cost of all Alfa Romeos on the list?
2. What is the count of all Fords on the list? Hint: use initial = 0
"""
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

# 1.
alfa_cost = reduce(
    lambda x, y: x + y,
    map(lambda car: car.price, filter(lambda car: car.make == "Alfa Romeo", cars)),
    0.0,
)
print(f"Total cost of all the Alfa Romeos on the list is {alfa_cost}.")
# Solution without using map-filter-reduce
alfa_cost = sum(car.price for car in cars if car.make == "Alfa Romeo")

# 2.
ford_count = reduce(lambda x, _: x + 1, filter(lambda car: car.make == "Ford", cars), 0)
print(f"The list contains {ford_count} Ford cars.")
# Solution without using map-filter-reduce
ford_count = len([car for car in cars if car.make == "Ford"])
