import unittest
from .utilities_test import *

runner = unittest.TextTestRunner()

utulities_test = unittest.TestLoader().loadTestsFromTestCase(Utilities_test)

runner.run(utulities_test)