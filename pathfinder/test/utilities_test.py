import unittest
from lib.utilities import Utilities

class Utilities_test(unittest.TestCase):
    def test_validate_instance_of(self):
        self.assertIsNone(Utilities.validate_instance_of("a", str))
        self.assertIsNone(Utilities.validate_instance_of(1, int))
        self.assertIsNone(Utilities.validate_instance_of(1.0, float))
        with self.assertRaises(TypeError): Utilities.validate_instance_of("a", int)
        with self.assertRaises(TypeError): Utilities.validate_instance_of(1, float)
        with self.assertRaises(TypeError): Utilities.validate_instance_of(1.0, str)

    def test_validate_nullable_instance_of(self):
        self.assertIsNone(Utilities.validate_nullable_instance_of(None, str))
        self.assertIsNone(Utilities.validate_nullable_instance_of(None, int))
        self.assertIsNone(Utilities.validate_nullable_instance_of(None, float))
        with self.assertRaises(TypeError): Utilities.validate_nullable_instance_of("a", int)
        with self.assertRaises(TypeError): Utilities.validate_nullable_instance_of(1, float)
        with self.assertRaises(TypeError): Utilities.validate_nullable_instance_of(1.0, str)

    def test_validate_latitude_and_longitude(self):
        with self.assertRaises(TypeError): Utilities.validate_latitude_and_longitude("a", "b")
        with self.assertRaises(TypeError): Utilities.validate_latitude_and_longitude(1, "b")
        with self.assertRaises(TypeError): Utilities.validate_latitude_and_longitude("a", 1)
        self.assertTrue(Utilities.validate_latitude_and_longitude(-90, -180))
        self.assertTrue(Utilities.validate_latitude_and_longitude(90, 180))
        self.assertTrue(Utilities.validate_latitude_and_longitude(5.12, 65.23))
        self.assertFalse(Utilities.validate_latitude_and_longitude(-91, -181))
        self.assertFalse(Utilities.validate_latitude_and_longitude(91.231, 181.456))