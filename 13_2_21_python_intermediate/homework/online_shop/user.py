from cart import Cart


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart(self)
        self.orders = []