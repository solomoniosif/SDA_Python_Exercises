import unittest

class TestBuiltins(unittest.TestCase):
    def test_membership(self):
        self.assertIn("A", "Animal")
        self.assertTrue("A" in "Animal")

    def test_instances(self):
        self.assertIsInstance(5, int)
        self.assertTrue(isinstance(5, int))

    def test_falsehood(self):
        self.assertFalse("X" in "Animal")



class TestTest(unittest.TestCase):
    def test_truehood(self):
        self.assertTrue(isinstance("5", str))
    
    def test_membership(self):
        self.assertTrue("n" in "Animal")



if __name__ == '__main__':
    unittest.main()