
# -Create Vehicle class with fields: name, type, color and value and methods: description() that
# returns a string describing the vehicle.
# -The Vehicle class initialization method should require name and price parameters and have
# default values for type and color.
# -Create vehicles list.
# -Write a loop that asks user 3 times for input regarding vehicle creation. With each loop
# iteration user should provide name and price and should be asked if he wants to provide type
# and color. If the user responds yes, he should be asked for the type and color. Once the input
# is collected, create new vehicle based on the input and add it to the vehicles list.
# -In a loop, print details of each car in the cars list.

class Vehicle():
    def __init__(self,name, price, v_type="car", color="black"):
        self.name = name
        self.price = price
        self.v_type = v_type
        self.color = color

    def description(self):
        return f"Vehicle {self.name} with price: ${self.price}, type: {self.v_type}, color: {self.color}."
    

vehicles = []
for i in range(3):
    name = input("Enter a name for the vehicle: ")
    price = input("Enter a price for the vehicle: ")
    custom_type_and_color = input("Would you like to add a custom type and color for the vehicle? Type 'yes' or 'no'. ")
    if custom_type_and_color == 'yes':
        v_type = input("Enter a type for the vehicle: ")
        color = input("Enter a color for the vehicle: ")
        vehicles.append(Vehicle(name, price, v_type, color))
    else:
        vehicles.append(Vehicle(name, price))

for vehicle in vehicles:
    print(vehicle.description())
