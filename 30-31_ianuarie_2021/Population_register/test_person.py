import unittest
import datetime
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.first_name = 'John'
        self.last_name = 'Cleese'
        self.birthdate = datetime.date(1939, 10, 27)

    def create_person_instance(self):
        return Person(first_name=self.first_name, last_name=self.last_name, birthdate=self.birthdate)

    def test_person_initialization(self):
        p = self.create_person_instance()
        self.assertEqual(p.first_name, 'John')
        self.assertEqual(p.last_name, 'Cleese')
        self.assertEqual(p.birthdate, datetime.date(1939, 10, 27))
        self.assertEqual(p.full_name, 'John Cleese')
        self.assertIsInstance(p.first_name, str)
        self.assertIsInstance(p.last_name, str)
        self.assertIsInstance(p.birthdate, datetime.date)

    def test_no_empty_name(self):
        self.first_name = ''
        with self.assertRaises(ValueError):
            self.create_person_instance()
        self.last_name = ''
        with self.assertRaises(ValueError):
            self.create_person_instance()

    def test_no_unallowed_charachters(self):
        self.first_name = "Eric*"
        with self.assertRaises(ValueError):
            self.create_person_instance()
        self.last_name = "|dle"
        with self.assertRaises(ValueError):
            self.create_person_instance()
        self.first_name = "Micha3l"
        with self.assertRaises(ValueError):
            self.create_person_instance()
        self.first_name = "Rich$"
        with self.assertRaises(ValueError):
            self.create_person_instance()

    def test_correct_name_formatting(self):
        self.first_name = "RONNIE  "
        self.last_name = "o'sullivan"
        p = self.create_person_instance()
        self.assertEqual(p.first_name, "Ronnie")
        self.assertEqual(p.last_name, "O'Sullivan")
        self.assertEqual(p.full_name, "Ronnie O'Sullivan")
        self.first_name = "Pedro     Daniel "
        self.last_name = "   Lorenza Gutierres"
        p = self.create_person_instance()
        self.assertEqual(p.first_name, "Pedro Daniel")
        self.assertEqual(p.last_name, "Lorenza Gutierres")
        self.assertEqual(p.full_name, "Pedro Daniel Lorenza Gutierres")

    def test_no_invalid_birthdate(self):
        self.birthdate = datetime.date(1623, 6, 19)
        with self.assertRaises(ValueError):
            self.create_person_instance()
        self.birthdate = datetime.date(2077, 1, 1)
        with self.assertRaises(ValueError):
            self.create_person_instance()

    def test_birthdate(self):
        p = self.create_person_instance()
        self.assertEqual(p.birthdate.year, 1939)
        self.assertEqual(p.birthdate.month, 10)
        self.assertEqual(p.birthdate.day, 27)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    