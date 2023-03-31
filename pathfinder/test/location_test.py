import unittest
from lib.location import Location

class Location_test(unittest.TestCase):
    def test_create_instance(self):
        self.assertIsInstance(Location(), Location)
        self.assertIsInstance(Location(address="Brisbane"), Location)
        self.assertIsInstance(Location(latitude = 27.4705, longitude = 153.0260), Location)
        self.assertIsInstance(Location(None, None, None), Location)
        with self.assertRaises(TypeError): Location(address=1)
        with self.assertRaises(TypeError): Location(address=1.1)
        with self.assertRaises(ValueError): Location(address = None, latitude = -91, longitude = -181)
        with self.assertRaises(ValueError): Location(address = None, latitude = 91.231, longitude = 181.456)
        with self.assertRaises(TypeError): Location(address = None, latitude = "a", longitude = "b")
        with self.assertRaises(TypeError): Location(address = None, latitude = 1, longitude = "b")
        with self.assertRaises(TypeError): Location(address = None, latitude = "a", longitude = 1)
        with self.assertRaises(TypeError): Location(address = None, latitude = None, longitude = 1)
        with self.assertRaises(TypeError): Location(address = None, latitude = 1, longitude = None)
        with self.assertRaises(TypeError): Location(address = None, latitude = None, longitude = "a")
        with self.assertRaises(TypeError): Location(address = None, latitude = "a", longitude = None)
    
    def test_getters_and_setters(self):
        location = Location()
        self.assertIsNone(location.address)
        self.assertIsNone(location.latitude)
        self.assertIsNone(location.longitude)
        with self.assertRaises(TypeError): location.address = 1
        with self.assertRaises(TypeError): location.address = 1.01
        with self.assertRaises(TypeError): location.address = Location()
        location.address = "Brisbane"
        self.assertEqual(location.address, "Brisbane")
        location.address = "Sydney"
        self.assertEqual(location.address, "Sydney")
        with self.assertRaises(ValueError): location.set_coordinates(-91, -181)
        with self.assertRaises(ValueError): location.set_coordinates(91.231, 181.456)
        with self.assertRaises(TypeError): location.set_coordinates("a", "b")
        with self.assertRaises(TypeError): location.set_coordinates(50, "b")
        with self.assertRaises(TypeError): location.set_coordinates("a", 50)
        with self.assertRaises(TypeError): location.set_coordinates(None, None)
        with self.assertRaises(TypeError): location.set_coordinates(50, None)
        with self.assertRaises(TypeError): location.set_coordinates(None, 50)
        with self.assertRaises(TypeError): location.set_coordinates(None, "b")
        with self.assertRaises(TypeError): location.set_coordinates("a", None)
        self.assertIsNone(location.set_coordinates(27.4705, 153.0260))
        self.assertEqual(location.latitude, 27.4705)
        self.assertEqual(location.longitude, 153.0260)
        self.assertIsNone(location.set_coordinates(33.8688, 151.2093))
        self.assertEqual(location.latitude, 33.8688)
        self.assertEqual(location.longitude, 151.2093)
        