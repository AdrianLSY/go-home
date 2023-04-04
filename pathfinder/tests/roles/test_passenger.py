import unittest
from lib.roles import Passenger

class Test_passenger(unittest.TestCase):

    def test_init(self):
        # Test valid input
        passenger = Passenger("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90)
        self.assertEqual(passenger.start_location.address, "123 Main St")
        self.assertEqual(passenger.start_location.latitude, 12.34)
        self.assertEqual(passenger.start_location.longitude, -45.67)
        self.assertEqual(passenger.end_location.address, "456 High St")
        self.assertEqual(passenger.end_location.latitude, 34.56)
        self.assertEqual(passenger.end_location.longitude, -78.90)

        # Test empty input
        passenger2 = Passenger()
        self.assertIsNone(passenger2.start_location.address)
        self.assertIsNone(passenger2.start_location.latitude)
        self.assertIsNone(passenger2.start_location.longitude)
        self.assertIsNone(passenger2.end_location.address)
        self.assertIsNone(passenger2.end_location.latitude)
        self.assertIsNone(passenger2.end_location.longitude)

        # Test partial input
        self.assertIsInstance(Passenger(None, 12.34, -45.67, "456 High St", 34.56, -78.90), Passenger)

        with self.assertRaises(TypeError):
            Passenger("123 Main St", None, -45.67, "456 High St", 34.56, -78.90)

        with self.assertRaises(TypeError):
            Passenger("123 Main St", 12.34, None, "456 High St", 34.56, -78.90)
        
        self.assertIsInstance(Passenger("123 Main St", None, None, "456 High St", 34.56, -78.90), Passenger)

        self.assertIsInstance(Passenger("123 Main St", 12.34, -45.67, None, 34.56, -78.90), Passenger)

        with self.assertRaises(TypeError):
            Passenger("123 Main St", 12.34, -45.67, "456 High St", None, -78.90)

        with self.assertRaises(TypeError):
            Passenger("123 Main St", 12.34, -45.67, "456 High St", 34.56, None)
        
        self.assertIsInstance(Passenger(None, 12.34, -45.67, "456 High St", None, None), Passenger)

        # Test invalid car_capacity input
        with self.assertRaises(TypeError):
            Passenger("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, "4")
        
        with self.assertRaises(TypeError):
            Passenger("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, None)
