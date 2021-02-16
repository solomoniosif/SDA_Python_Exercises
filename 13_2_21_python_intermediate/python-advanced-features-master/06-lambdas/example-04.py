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

# Let's find the price of the cheapest Citroën on the list
c = reduce(
    min, map(lambda car: car.price, filter(lambda car: car.make == "Citroën", cars))
)
print(f"The cheapest Citroën costs: {c}")
