import numbers

class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = self.validate_bool(in_stock)
        self.categories = list()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self.validate_and_set_string(name, "Name")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = self.validate_and_set_price(price)

    def add_category(self, category):
        category = self.validate_and_set_string(category, "Category", max_length=30)
        if category not in self.categories:
            self.categories.append(category)

    def remove_category(self, category):
        if category in self.categories:
            self.categories.remove(category)

    def apply_discount(self, discount):
        '''Discount can be either from 0 to 1 (exclusive) or from 1 to 100 (inclusive). Ex. Discount of 0.3 = 30%, and discount of 30 is also 30%'''
        if not isinstance(discount, numbers.Real):
            raise ValueError('Discount must be a real number.')
        if discount > 0 and discount < 1:
            new_price = self._price - (self._price * discount)
            self._price = self.validate_and_set_price(new_price)
        elif discount >= 1 and discount <= 100:
            new_price = self._price - (self._price * discount/100)
            self._price = self.validate_and_set_price(new_price)
        else:
            raise ValueError('Discount can be either between 0 and 1 or 1 and 100.')

    def is_in_stock(self):
        return self.in_stock

    def __repr__(self):
        return f"<Product> Name: {self.name} | Price: ${round(self.price, 2)} | Currently {'' if self.in_stock else 'not '}in stock."

    @staticmethod
    def validate_and_set_string(value, field_name, max_length=100):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f"{field_name.capitalize()} cannot be empty")
        if len(value.strip()) > max_length:
            raise ValueError(f'The length of the name cannot be greather than {max_length}.')
        if value.isdigit():
            raise ValueError(f"{field_name.capitalize()} cannot be only digits.")
        return str(value).strip()
    
    @staticmethod
    def validate_and_set_price(price, min_price=0.1):
        if not isinstance(price, numbers.Real):
            raise ValueError('Price must be a real number.')
        if min_price is not None and price < min_price:
            raise ValueError(f'Price must be at least {min_price}.')
        return float(price)

    @staticmethod
    def validate_bool(value):
        if not isinstance(value, bool):
            raise ValueError('This value must be a boolean.')
        return bool(value)



##################################################################
yoga_slim_7 = Product('Lenovo Yoga Slim 7', 1049, True)

print(yoga_slim_7)

yoga_slim_7.apply_discount(30)

print(yoga_slim_7)

yoga_slim_7.add_category('Laptops')
yoga_slim_7.add_category('  Laptops     ')
print(yoga_slim_7.categories)