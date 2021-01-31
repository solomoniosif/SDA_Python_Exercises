
class Product():
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.category = []

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount)

    def add_category(self, category):
        self.category.append(category)

    def remove_category(self, category):
        if category in self.category:
            self.category.remove(category)

    def is_in_stock(self):
        return self.in_stock

    def __repr__(self):
        return f"Product: {self.name} with the price: ${self.price} currently {'' if self.in_stock else 'not '}in stock."

