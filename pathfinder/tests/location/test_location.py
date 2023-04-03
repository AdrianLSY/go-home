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
        loc3 = Location(None, 12.34, -45.67)
        self.assertIsNone(loc3.address)
        self.assertEqual(loc3.latitude, 12.34)
        self.assertEqual(loc3.longitude, -45.67)

        loc3 = Location("123 Main St", None, None)
        self.assertEqual(loc.address, "123 Main St")
        self.assertEqual(loc3.latitude, None)
        self.assertEqual(loc3.longitude, None)

        # Test incomplete latitude and longitude
        with self.assertRaises(TypeError):
            loc4 = Location(None, None, -78.90)

        with self.assertRaises(TypeError):
            loc4 = Location(None, 34.56, None)

        # Test invalid input types
        with self.assertRaises(TypeError):
            loc4 = Location(None, "34.56", -78.90)

        with self.assertRaises(TypeError):
            loc4 = Location(None, 34.56, "-78.90")

        # Test invalid coordinates
        with self.assertRaises(ValueError):
            loc4 = Location(None, 91, -78.90)

        with self.assertRaises(ValueError):
            loc4 = Location(None, 34.56, -181)

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
