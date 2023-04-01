import unittest
from lib.utility import Utility

class Test_is_between(unittest.TestCase):
    
    def test_valid_input(self):
        Utility.is_between(5, 1, 10)  # Should not raise an exception
        Utility.is_between(1, 1, 10)  # Should not raise an exception
        Utility.is_between(10, 1, 10)  # Should not raise an exception
        Utility.is_between(5.5, 1.0, 10.0)  # Should not raise an exception
        Utility.is_between(5, 1.0, 10.0)  # Should not raise an exception

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Utility.is_between(0, 1, 10)
        with self.assertRaises(ValueError):
            Utility.is_between(11, 1, 10)
        with self.assertRaises(ValueError):
            Utility.is_between(5, 10, 1)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Utility.is_between("5", 1, 10)
        with self.assertRaises(TypeError):
            Utility.is_between(5, "1", 10)
        with self.assertRaises(TypeError):
            Utility.is_between(5, 1, "10")
        with self.assertRaises(TypeError):
            Utility.is_between(5, None, 10)
        with self.assertRaises(TypeError):
            Utility.is_between(5, 1, None)

    def test_edge_cases(self):
        Utility.is_between(0.0, 0.0, 0.0)  # Should not raise an exception
        Utility.is_between(-5, -10, 0)  # Should not raise an exception
        Utility.is_between(-5, -10, 0.0)  # Should not raise an exception
        Utility.is_between(-0.1, -0.5, 0.0)  # Should not raise an exception

        with self.assertRaises(ValueError):
            Utility.is_between(0.1, 0.0, 0.0)
        with self.assertRaises(ValueError):
            Utility.is_between(-5.5, -5, -1)
