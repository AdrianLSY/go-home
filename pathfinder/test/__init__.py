import unittest

tests = []

from .utility_test import *
tests.append(unittest.TestLoader().loadTestsFromTestCase(Utility_test))

from .location_test import *
tests.append(unittest.TestLoader().loadTestsFromTestCase(Location_test))

runner = unittest.TextTestRunner()
[runner.run(test) for test in tests]
