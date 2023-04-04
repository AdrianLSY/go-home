import unittest
from lib.roles import Roles, Walk, Driver, Passenger

class TestRoles(unittest.TestCase):

    def test_roles_enum(self):
        # Test that walk role is associated with Walk class
        self.assertIsInstance(Roles.walk.value, Walk)

        # Test that driver role is associated with Driver class
        self.assertIsInstance(Roles.driver.value, Driver)

        # Test that passenger role is associated with Passenger class
        self.assertIsInstance(Roles.passenger.value, Passenger)
