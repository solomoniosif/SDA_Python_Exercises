import datetime

from invoice import Invoice


class Cart:
    def __init__(self, user, products=dict()):
        self.user = user
        self.products = products

    def add_to_cart(self, product, quantity):
        if product not in self.products:
            self.products[product] = quantity
        self.products[product] += quantity

    def buy_products_in_cart(self):
        invoice = Invoice.generate_invoice(self.user.cart)
        order = {datetime.datetime.now(): self.user.cart.products}
        if invoice:
            self.user.orders.append(order)
            self.user.cart.products = []