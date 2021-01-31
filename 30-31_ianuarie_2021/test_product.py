import unittest
from product_2 import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.name = 'Lenovo Yoga Slim 7'
        self.price = 1049
        self.in_stock = True

    # * Helper method. Creates a Product instance with arguments initialized in setUp method that can be overwritten by each test as needed.
    def create_product_instance(self):
        p = Product(self.name, self.price, self.in_stock)
        return p

    # * Tests object initialization with arguments created in setUp method.
    def test_create_product(self): 
        p = self.create_product_instance()
        self.assertEqual(p.name, self.name)
        self.assertEqual(p.price, self.price)
        self.assertEqual(p.in_stock, self.in_stock)
        self.assertTrue(len(p.categories) == 0)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.price, float)
        self.assertIsInstance(p.in_stock, bool)
        self.assertIsInstance(p.categories, list)

    # * Tests failure to initialize product with empty name string
    def test_no_empty_name(self):
        self.name = ''
        with self.assertRaises(ValueError):
            p = self.create_product_instance()

    # * Tests product is initialized with stripped name
    def test_name_is_stripped(self):
        self.name = '  Lenovo Yoga   '
        p = self.create_product_instance()
        self.assertEqual(p.name, self.name.strip())
        self.assertNotEqual(p.name[0], ' ')
        self.assertNotEqual(p.name[-1], ' ')

    # * Tests failure to initialize product with name set as None
    def test_name_not_None(self):
        self.name = None
        with self.assertRaises(ValueError):
            p = self.create_product_instance()

    # * Tests failure to initialize product with name longer than max_length set in Product class
    def test_len_name_not_greater_than_max(self):
        self.name = 'The sleek Spirit II E-210 gas grill. This two burner grill is built to fit small spaces, and packed with features such as the powerful GS4 grilling system, iGrill capability, and convenient side tables for placing serving trays. Welcome to the Weber family.'
        with self.assertRaises(ValueError):
            p = self.create_product_instance()
            self.assertEqual(len(p.name), 0)

    # * Tests failure to initialize product with name consisting of digits only
    def test_name_not_digits_only(self):
        self.name = '123456789'
        with self.assertRaises(ValueError):
            p = self.create_product_instance()

    # * Tests failure to initialize product with price as string
    def test_price_not_string(self):
        self.price = 'one thousand'
        with self.assertRaises(ValueError):
            p = self.create_product_instance()

    # * Tests failure to initialize product with price smaller than min_price set in Product class or negative price
    def test_price_not_smaller_than_min_or_negative(self):
        self.price = -20
        with self.assertRaises(ValueError):
            p = self.create_product_instance()

    # * Tests failure to aply a negative discount
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            p = self.create_product_instance()
            p.apply_discount(-30)

    # * Tests failure to aply a discount outside given parameters in Product class
    def test_invalid_discount_2(self):
        with self.assertRaises(ValueError):
            p = self.create_product_instance()
            p.apply_discount(110)
    
    # * Tests failure to aply discount if discount is given as string that cannot be converted to int or float
    def test_invalid_discount_3(self):
        with self.assertRaises(ValueError):
            p = self.create_product_instance()
            p.apply_discount('trei zeci')

    # * Test correct price adjustment after appling discount
    def test_price_after_discount(self):
        p = self.create_product_instance()
        p.apply_discount(0.3)
        self.assertEqual(p.price, self.price - (self.price * 0.3))

    # * Tests failure to initialize product with with a given argument for in_stock other than boolean
    def test_in_stock_is_bool(self):
        self.in_stock = 'Out of stock'
        with self.assertRaises(ValueError):
            p = self.create_product_instance()

    # * Tests category added successfully
    def test_category_added(self):
        p = self.create_product_instance()
        p.add_category('Laptops')
        self.assertIn('Laptops', p.categories)

    # * Tests failure to add category if it consists of digits only
    def test_category_not_digits_only(self):
        p = self.create_product_instance()
        with self.assertRaises(ValueError):
            p.add_category('12345678')

    # * Tests failure to add category if it's length exceeds max_length provided in Produst class
    def test_category_length_not_greather_than_max(self):
        p = self.create_product_instance()
        with self.assertRaises(ValueError):
            p.add_category('Laptops, Personal computers, tablets, smartphones and many other devices that you can use at home or at work')

    # * Tests for duplicates categories
    def test_no_duplicate_categories(self):
        p = self.create_product_instance()
        p.add_category('Laptops')
        p.add_category('Laptops')
        self.assertTrue(p.categories.count('Laptops') == 1)
        self.assertEqual(len(p.categories), 1)

    # * Tests if category has been removed succesfully
    def test_category_removed(self):
        p = self.create_product_instance()
        p.add_category('Laptops')
        p.remove_category('Laptops')
        self.assertNotIn('Laptops', p.categories)
        self.assertEqual(len(p.categories), 0)

    # * Tests if ValueError is raised when trying to remove a nonexistent category
    def test_remove_nonexistent_category(self):
        p = self.create_product_instance()
        with self.assertRaises(ValueError):
            p.remove_category('Laptops')

    # * Tests the correct output of is_in_stock method
    def test_is_in_stock(self):
        p = self.create_product_instance()
        p.in_stock = False
        self.assertEqual(p.is_in_stock(), False)
        p.in_stock = True
        self.assertEqual(p.is_in_stock(), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)