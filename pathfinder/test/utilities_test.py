import unittest
from lib.utilities import Utilities

class Utilities_test(unittest.TestCase):
    def test_validate_instance_of(self, object, a_class):
        self.assertIsNone(Utilities.validate_instance_of("a", str))
        self.assertIsNone(Utilities.validate_instance_of(1, int))
        self.assertIsNone(Utilities.validate_instance_of(1, float))


if __name__ == '__main__':
    unittest.main()