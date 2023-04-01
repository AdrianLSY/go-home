import unittest
from lib.utility import Utility

class TestCheckSmaller(unittest.TestCase):

    def test_valid_input(self):
        Utility.check_smaller(5, 10)  # Should not raise an exception
        Utility.check_smaller(5.5, 10.5)  # Should not raise an exception
        Utility.check_smaller(5, 10.0)  # Should not raise an exception
        Utility.check_smaller(5.0, 10)  # Should not raise an exception

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Utility.check_smaller(10, 5)
        with self.assertRaises(ValueError):
            Utility.check_smaller(10.5, 5.5)
        with self.assertRaises(ValueError):
            Utility.check_smaller(5, 5)
        with self.assertRaises(ValueError):
            Utility.check_smaller(5.0, 5.0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Utility.check_smaller("5", 10)
        with self.assertRaises(TypeError):
            Utility.check_smaller(5, "10")
        with self.assertRaises(TypeError):
            Utility.check_smaller(None, 10)
        with self.assertRaises(TypeError):
            Utility.check_smaller(5, None)

    def test_edge_cases(self):
        Utility.check_smaller(-10, -5)  # Should not raise an exception
        Utility.check_smaller(-5, 0)  # Should not raise an exception
        Utility.check_smaller(0, 0.1)  # Should not raise an exception

        with self.assertRaises(ValueError):
            Utility.check_smaller(-5, -10)
        with self.assertRaises(ValueError):
            Utility.check_smaller(0, -5)