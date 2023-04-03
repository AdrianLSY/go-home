import unittest
from lib.graph import Person
from lib.roles import Roles

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person1 = Person("Alice", "555-555-1234", role=Roles.walk)
        self.person2 = Person("Bob", "555-555-5678", role=Roles.passenger)

    def test_init(self):
        self.assertEqual(self.person1.name, "Alice")
        self.assertEqual(self.person1.phone, "555-555-1234")
        self.assertEqual(self.person1.role, Roles.walk)

        self.assertEqual(self.person2.name, "Bob")
        self.assertEqual(self.person2.phone, "555-555-5678")
        self.assertEqual(self.person2.role, Roles.passenger)

    def test_invalid_init(self):
        with self.assertRaises(TypeError):
            Person(123, "555-555-1234", Roles.walk)
        with self.assertRaises(TypeError):
            Person("Alice", 5555551234, Roles.walk)
        with self.assertRaises(TypeError):
            Person("Alice", "555-555-1234", "walk")
        with self.assertRaises(TypeError):
            Person(None, "555-555-1234", role=Roles.walk)
        with self.assertRaises(TypeError):
            Person("Alice", None, role=Roles.walk)
        with self.assertRaises(TypeError):
            Person("Alice", "555-555-1234", role=None)

    def test_set_name(self):
        self.person1.name = "Alicia"
        self.assertEqual(self.person1.name, "Alicia")

    def test_set_invalid_name(self):
        with self.assertRaises(TypeError):
            self.person1.name = 123
        with self.assertRaises(TypeError):
            self.person1.name = None

    def test_set_phone(self):
        self.person1.phone = "555-555-4321"
        self.assertEqual(self.person1.phone, "555-555-4321")

    def test_set_invalid_phone(self):
        with self.assertRaises(TypeError):
            self.person1.phone = 5555554321
        with self.assertRaises(TypeError):
            self.person1.phone = None

    def test_set_role(self):
        self.person1.role = Roles.driver
        self.assertEqual(self.person1.role, Roles.driver)

    def test_set_invalid_role(self):
        with self.assertRaises(TypeError):
            self.person1.role = "driver"
        with self.assertRaises(TypeError):
            self.person1.role = None
