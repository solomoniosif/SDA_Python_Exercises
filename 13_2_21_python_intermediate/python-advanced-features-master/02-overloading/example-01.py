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
        if isinstance(other, EshopCart):
            self.products.extend(other.products)
            self.total += other.total
            return self

    def __contains__(self, item):
        return item in self.products

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.total == other.total

    def __str__(self):
        return f"EshopCart{{buyer:{self.buyer}, total:{self.total}, products:{len(self)}}}" #.format(self.buyer, self.total, self.products)

    def __repr__(self):
        return f"EshopCart(buyer={self.buyer})"



if __name__ == "__main__":
    cart = EshopCart("Ann")
    cart.add_product("jeans", 30.0)
    print(f"Cart's length: {len(cart)}")

    print(cart)
