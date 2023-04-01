import unittest
from lib.location import Location

class Test_location(unittest.TestCase):

    def test_init(self):
        # Test valid input
        loc = Location("123 Main St", 12.34, -45.67)
        self.assertEqual(loc.address, "123 Main St")
        self.assertEqual(loc.latitude, 12.34)
        self.assertEqual(loc.longitude, -45.67)

        # Test empty input
        loc2 = Location()
        self.assertIsNone(loc2.address)
        self.assertIsNone(loc2.latitude)
        self.assertIsNone(loc2.longitude)

        # Test partial input
        loc3 = Location("123 Main St", None, -45.67)
        self.assertEqual(loc3.address, "123 Main St")
        self.assertIsNone(loc3.latitude)
        self.assertEqual(loc3.longitude, -45.67)

        loc4 = Location("123 Main St", 12.34, None)
        self.assertEqual(loc4.address, "123 Main St")
        self.assertEqual(loc4.latitude, 12.34)
        self.assertIsNone(loc4.longitude)

        loc5 = Location(None, 12.34, -45.67)
        self.assertIsNone(loc5.address)
        self.assertEqual(loc5.latitude, 12.34)
        self.assertEqual(loc5.longitude, -45.67)

        # Test invalid input types
        with self.assertRaises(TypeError):
            Location(123, 12.34, -45.67)

        with self.assertRaises(TypeError):
            Location("123 Main St", "12.34", -45.67)

        with self.assertRaises(TypeError):
            Location("123 Main St", 12.34, "-45.67")

        # Test invalid coordinates
        with self.assertRaises(ValueError):
            Location("123 Main St", 91, -45.67)

        with self.assertRaises(ValueError):
            Location("123 Main St", 12.34, -181)

    def test_address_setter(self):
        loc = Location()

        # Test valid input
        loc.address = "456 High St"
        self.assertEqual(loc.address, "456 High St")

        # Test setting address to None
        loc.address = None
        self.assertIsNone(loc.address)

        # Test invalid input
        with self.assertRaises(TypeError):
            loc.address = 123

    def test_set_coordinates(self):
        loc = Location()

        # Test valid input
        loc.set_coordinates(34.56, -78.90)
        self.assertEqual(loc.latitude, 34.56)
        self.assertEqual(loc.longitude, -78.90)

        # Test setting coordinates to None
        loc.set_coordinates(None, None)
        self.assertIsNone(loc.latitude)
        self.assertIsNone(loc.longitude)

        # Test setting only one coordinate to None
        with self.assertRaises(TypeError):
            loc.set_coordinates(None, -78.90)

        with self.assertRaises(TypeError):
            loc.set_coordinates(34.56, None)

        # Test invalid input types
        with self.assertRaises(TypeError):
            loc.set_coordinates("34.56", -78.90)

        with self.assertRaises(TypeError):
            loc.set_coordinates(34.56, "-78.90")

        # Test invalid coordinates
        with self.assertRaises(ValueError):
            loc.set_coordinates(91, -78.90)

        with self.assertRaises(ValueError):
            loc.set_coordinates(34.56, -181)
