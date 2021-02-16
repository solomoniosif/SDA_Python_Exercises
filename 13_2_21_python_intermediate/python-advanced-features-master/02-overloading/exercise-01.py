class EshopCart:
    def __init__(self, buyer):
        self.buyer = buyer
        self.products = []
        self.total = 0.0

    def add_product(self, name, price):
        self.products.append(name)
        self.total += price

    def __len__(self):
        return len(self.products)

    def __add__(self, other):
        self.products.extend(other.products)
        self.total += other.total
        return self

    def __lt__(self, other):
        return self.total < other.total

    def __gt__(self, other):
        return self.total > other.total

    def __eq__(self, other):
        return self.total == other.total

    def __str__(self):
        return f"EshopCart{{buyer: {self.buyer}, total: {self.total}, products: {len(self)}}}"


if __name__ == "__main__":
    cart = EshopCart("Ann")
    cart.add_product("jeans", 30.0)

    cart2 = EshopCart("Ann")
    cart2.add_product("shirt", 15.30)

    cart = cart + cart2
    print(str(cart))
    print(f"Cart's length: {len(cart)}")
    print(f"Cart's contents: {cart.products}")
    print(f"Total: {cart.total}")
    print(f"cart > cart2: {cart > cart2}")
