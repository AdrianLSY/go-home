import unittest
from lib.utility import Utility

class Test_validate_latitude_and_longitude(unittest.TestCase):

    def test_valid_input(self):
        Utility.validate_latitude_and_longitude(0, 0)  # Should not raise an exception
        Utility.validate_latitude_and_longitude(-90, -180)  # Should not raise an exception
        Utility.validate_latitude_and_longitude(90, 180)  # Should not raise an exception
        Utility.validate_latitude_and_longitude(45.5, -135.5)  # Should not raise an exception
        Utility.validate_latitude_and_longitude(-45.5, 135.5)  # Should not raise an exception

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Utility.validate_latitude_and_longitude(90.1, 0)
        with self.assertRaises(ValueError):
            Utility.validate_latitude_and_longitude(0, 180.1)
        with self.assertRaises(ValueError):
            Utility.validate_latitude_and_longitude(-90.1, 0)
        with self.assertRaises(ValueError):
            Utility.validate_latitude_and_longitude(0, -180.1)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Utility.validate_latitude_and_longitude("45", 0)
        with self.assertRaises(TypeError):
            Utility.validate_latitude_and_longitude(45, "0")
        with self.assertRaises(TypeError):
            Utility.validate_latitude_and_longitude(None, 0)
        with self.assertRaises(TypeError):
            Utility.validate_latitude_and_longitude(45, None)

    def test_edge_cases(self):
        Utility.validate_latitude_and_longitude(-90.0, 180.0)  # Should not raise an exception
        Utility.validate_latitude_and_longitude(90.0, -180.0)  # Should not raise an exception
        Utility.validate_latitude_and_longitude(0.0, 0.0)  # Should not raise an exception

        with self.assertRaises(ValueError):
            Utility.validate_latitude_and_longitude(90.00001, 0)
        with self.assertRaises(ValueError):
            Utility.validate_latitude_and_longitude(0, 180.00001)
