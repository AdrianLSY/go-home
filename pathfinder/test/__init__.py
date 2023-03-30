import unittest
from .utility_test import *

runner = unittest.TextTestRunner()

utulities_test = unittest.TestLoader().loadTestsFromTestCase(Utility_test)

runner.run(utulities_test)