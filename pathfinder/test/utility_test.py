import unittest
from lib.utility import Utility

class Utility_test(unittest.TestCase):
    def test_validate_instance_of(self):
        # Test if the function returns None if the data type is the same
        self.assertIsNone(Utility.validate_instance_of("a", str))
        self.assertIsNone(Utility.validate_instance_of(1, int))
        self.assertIsNone(Utility.validate_instance_of(1.0, float))
        self.assertIsNone(Utility.validate_instance_of(True, bool))
        self.assertIsNone(Utility.validate_instance_of(False, bool))
        self.assertIsNone(Utility.validate_instance_of(1.0, (int, float)))
        self.assertIsNone(Utility.validate_instance_of(1, (int, float)))

        # Test if the function raises a TypeError if the data type is not the same
        with self.assertRaises(TypeError): Utility.validate_instance_of("a", int)
        with self.assertRaises(TypeError): Utility.validate_instance_of(1, float)
        with self.assertRaises(TypeError): Utility.validate_instance_of(1.0, str)
        with self.assertRaises(TypeError): Utility.validate_instance_of(True, int)
        with self.assertRaises(TypeError): Utility.validate_instance_of(False, int)
        with self.assertRaises(TypeError): Utility.validate_instance_of(1, bool)
        with self.assertRaises(TypeError): Utility.validate_instance_of(0, bool)
        with self.assertRaises(TypeError): Utility.validate_instance_of(True, float)
        with self.assertRaises(TypeError): Utility.validate_instance_of(False, float)
        with self.assertRaises(TypeError): Utility.validate_instance_of("a", (int, float))
        with self.assertRaises(TypeError): Utility.validate_instance_of(True, (int, float))
        with self.assertRaises(TypeError): Utility.validate_instance_of(False, (int, float))

    def test_validate_nullable_instance_of(self):
        # Test if the function returns None if the data type is None, regardless of specified data type to compare to
        self.assertIsNone(Utility.validate_nullable_instance_of(None, str))
        self.assertIsNone(Utility.validate_nullable_instance_of(None, int))
        self.assertIsNone(Utility.validate_nullable_instance_of(None, float))
        self.assertIsNone(Utility.validate_nullable_instance_of(None, bool))

        # Test if the function raises a TypeError if the data type is not the same
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of("a", int)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(1, float)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(1.0, str)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(True, int)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(False, int)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(1, bool)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(0, bool)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(True, float)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(False, float)
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of("a", (int, float))
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(True, (int, float))
        with self.assertRaises(TypeError): Utility.validate_nullable_instance_of(False, (int, float))


    def test_validate_latitude_and_longitude(self):
        # Test valid geographical ranges
        self.assertIsNone(Utility.validate_latitude_and_longitude(-90, -180))
        self.assertIsNone(Utility.validate_latitude_and_longitude(90, 180))
        self.assertIsNone(Utility.validate_latitude_and_longitude(5.12, 65.23))

        # Test invalid ranges
        with self.assertRaises(ValueError): Utility.validate_latitude_and_longitude(-91, -181)
        with self.assertRaises(ValueError): Utility.validate_latitude_and_longitude(91.231, 181.456)
        with self.assertRaises(ValueError): Utility.validate_latitude_and_longitude(50, 181.456)
        with self.assertRaises(ValueError): Utility.validate_latitude_and_longitude(91.231, 50)

        # Test Invalid types
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude("a", "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude(1, "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude("a", 1)
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude(True, "b")
        with self.assertRaises(TypeError): Utility.validate_latitude_and_longitude(1, False)
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

    def test_check_bigger(self):
        # Test that the function returns None if the number is bigger than the threshold.
        self.assertIsNone(Utility.check_bigger(10, 5))
        self.assertIsNone(Utility.check_bigger(-5, -10))
        self.assertIsNone(Utility.check_bigger(0, -10))
        self.assertIsNone(Utility.check_bigger(3.14, -2.71))
        self.assertIsNone(Utility.check_bigger(-7.5, -8.0))

        # Test that the function raises a ValueError if the number is not bigger than the threshold.
        with self.assertRaises(ValueError): Utility.check_bigger(5, 10)
        with self.assertRaises(ValueError): Utility.check_bigger(-10, -5)
        with self.assertRaises(ValueError): Utility.check_bigger(-5, 0)
        with self.assertRaises(ValueError): Utility.check_bigger(-2.71, 3.14)
        with self.assertRaises(ValueError): Utility.check_bigger(-8.0, -7.5)

        # Test that the function raises a TypeError if either number or threshold is not a float or int.
        with self.assertRaises(TypeError): Utility.check_bigger("5", 10)
        with self.assertRaises(TypeError): Utility.check_bigger(5, "10")
        with self.assertRaises(TypeError): Utility.check_bigger(True, 10)
        with self.assertRaises(TypeError): Utility.check_bigger(5, None)

    def test_check_smaller(self):
        # Test that the function returns None if the number is smaller than the threshold.
        self.assertIsNone(Utility.check_smaller(5, 10))
        self.assertIsNone(Utility.check_smaller(-10, -5))
        self.assertIsNone(Utility.check_smaller(-10, 0))
        self.assertIsNone(Utility.check_smaller(-2.71, 3.14))
        self.assertIsNone(Utility.check_smaller(-8.0, -7.5))

        # Test that the function raises a ValueError if the number is not smaller than the threshold.
        with self.assertRaises(ValueError): Utility.check_smaller(10, 5)
        with self.assertRaises(ValueError): Utility.check_smaller(-5, -10)
        with self.assertRaises(ValueError): Utility.check_smaller(0, -10)
        with self.assertRaises(ValueError): Utility.check_smaller(3.14, -2.71)
        with self.assertRaises(ValueError): Utility.check_smaller(-7.5, -8.0)

        # Test that the function raises a TypeError if either number or threshold is not a float or int.
        with self.assertRaises(TypeError): Utility.check_smaller("5", 10)
        with self.assertRaises(TypeError): Utility.check_smaller(5, "10")
        with self.assertRaises(TypeError): Utility.check_smaller(True, 10)
        with self.assertRaises(TypeError): Utility.check_smaller(5, None)
