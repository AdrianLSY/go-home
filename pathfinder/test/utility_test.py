import unittest
from lib.utility import Utility

class Utility_test(unittest.TestCase):
    def test_validate_instance_of(self):
        self.assertIsNone(Utility.validate_instance_of("a", str))
        self.assertIsNone(Utility.validate_instance_of(1, int))
        self.assertIsNone(Utility.validate_instance_of(1.0, float))
        with self.assertRaises(TypeError): Utility.validate_instance_of("a", int)
        with self.assertRaises(TypeError): Utility.validate_instance_of(1, float)
        with self.assertRaises(TypeError): Utility.validate_instance_of(1.0, str)

    def test_validate_nullable_instance_of(self):
        self.assertIsNone(Utility.validate_nullable_instance_of(None, str))
        self.assertIsNone(Utility.validate_nullable_instance_of(None, int))
        self.assertIsNone(Utility.validate_nullable_instance_of(None, float))
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of("a", int)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(1, float)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(1.0, str)

    def test_validate_latitude_and_longitude(self):
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude("a", "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude(1, "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude("a", 1)
        self.assertIsNone(Utility.validate_latitude_and_longitude(-90, -180))
        self.assertIsNone(Utility.validate_latitude_and_longitude(90, 180))
        self.assertIsNone(Utility.validate_latitude_and_longitude(5.12, 65.23))
        with self.assertRaises(ValueError): Utility.validate_latitude_and_longitude(-91, -181)
        with self.assertRaises(ValueError): Utility.validate_latitude_and_longitude(91.231, 181.456)
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude("a", "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude(1, "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude("a", 1)

    def test_validate_nullable_latitude_and_longitude(self):
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude("a", "b")
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude(1, "b")
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude("a", 1)
        self.assertIsNone(Utility.validate_nullable_latitude_and_longitude(-90, -180))
        self.assertIsNone(Utility.validate_nullable_latitude_and_longitude(90, 180))
        self.assertIsNone(Utility.validate_nullable_latitude_and_longitude(5.12, 65.23))
        with self.assertRaises(ValueError): Utility.validate_nullable_latitude_and_longitude(-91, -181)
        with self.assertRaises(ValueError): Utility.validate_nullable_latitude_and_longitude(91.231, 181.456)
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude("a", "b")
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude(1, "b")
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude("a", 1)
        self.assertIsNone(Utility.validate_nullable_latitude_and_longitude(None, None))
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude(None, 1)
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude(1, None)
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude(None, "a")
        with self.assertRaises(TypeError): Utility.validate_nullable_latitude_and_longitude("a", None)
    
    def test_is_between(self):
        self.assertIsNone(Utility.is_between(50, 1, 100))
        self.assertIsNone(Utility.is_between(-50 ,-100, -1))
        self.assertIsNone(Utility.is_between(1 , 1, 1))
        self.assertIsNone(Utility.is_between(-1 , -1, -1))
        with self.assertRaises(ValueError): Utility.is_between(75, 100, 50)
        with self.assertRaises(ValueError): Utility.is_between(-75, -50, -100)
        with self.assertRaises(ValueError): Utility.is_between(75, 100, 50)
        with self.assertRaises(ValueError): Utility.is_between(-75, -50, -100)
        with self.assertRaises(TypeError): Utility.is_between("a", "b", "c")
        with self.assertRaises(TypeError): Utility.is_between(1, "b", "c")
        with self.assertRaises(TypeError): Utility.is_between("a", 1, "c")
        with self.assertRaises(TypeError): Utility.is_between(1, 1, "c")
        with self.assertRaises(TypeError): Utility.is_between("a", "b", 1)
        with self.assertRaises(TypeError): Utility.is_between(1, "b", 1)
        with self.assertRaises(TypeError): Utility.is_between("a", 1, 1)
        