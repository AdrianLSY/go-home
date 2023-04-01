import os
import unittest


# Initialize a TestSuite to collect all the tests
tests = unittest.TestSuite()

# Searches all directories and collects all test suites found inside the subdirectory
for directory in [directory for directory in os.listdir(os.path.dirname(os.path.abspath(__file__))) if os.path.isdir(f"{os.path.dirname(os.path.abspath(__file__))}/{directory}") and directory != '__pycache__']:
    tests.addTests(unittest.TestLoader().discover(f"{os.path.dirname(os.path.abspath(__file__))}/{directory}"))

# Run all tests in the collected TestSuite
os.system('cls' if os.name == 'nt' else 'clear')
print("Running test suites")
print("----------------------------------------------------------------------\n")
unittest.TextTestRunner(verbosity=2).run(tests)
print("----------------------------------------------------------------------")
