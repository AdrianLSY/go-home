import os
import unittest

# Searches all directories inside tests/ and runs all test suites found inside the subdirectory
for directory in [directory for directory in os.listdir(f"{os.path.dirname(os.path.abspath(__file__))}") if os.path.isdir(os.path.join(f"{os.path.dirname(os.path.abspath(__file__))}", directory)) and directory != '__pycache__']:
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover(f"{os.path.dirname(os.path.abspath(__file__))}/{directory}"))