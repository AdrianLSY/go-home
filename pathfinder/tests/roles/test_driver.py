import unittest
from lib.roles import Driver

class Test_driver(unittest.TestCase):

    def test_init(self):
        # Test valid input
        driver = Driver("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, 4)
        self.assertEqual(driver.start_location.address, "123 Main St")
        self.assertEqual(driver.start_location.latitude, 12.34)
        self.assertEqual(driver.start_location.longitude, -45.67)
        self.assertEqual(driver.end_location.address, "456 High St")
        self.assertEqual(driver.end_location.latitude, 34.56)
        self.assertEqual(driver.end_location.longitude, -78.90)
        self.assertEqual(driver.car_capacity, 4)

        # Test empty input
        driver2 = Driver()
        self.assertIsNone(driver2.start_location.address)
        self.assertIsNone(driver2.start_location.latitude)
        self.assertIsNone(driver2.start_location.longitude)
        self.assertIsNone(driver2.end_location.address)
        self.assertIsNone(driver2.end_location.latitude)
        self.assertIsNone(driver2.end_location.longitude)
        self.assertEqual(driver2.car_capacity, 0)

        # Test partial input
        self.assertIsInstance(Driver(None, 12.34, -45.67, "456 High St", 34.56, -78.90, 4), Driver)

        with self.assertRaises(TypeError):
            Driver("123 Main St", None, -45.67, "456 High St", 34.56, -78.90, 4)

        with self.assertRaises(TypeError):
            Driver("123 Main St", 12.34, None, "456 High St", 34.56, -78.90, 4)
        
        self.assertIsInstance(Driver("123 Main St", None, None, "456 High St", 34.56, -78.90, 4), Driver)

        self.assertIsInstance(Driver("123 Main St", 12.34, -45.67, None, 34.56, -78.90, 4), Driver)

        with self.assertRaises(TypeError):
            Driver("123 Main St", 12.34, -45.67, "456 High St", None, -78.90, 4)

        with self.assertRaises(TypeError):
            Driver("123 Main St", 12.34, -45.67, "456 High St", 34.56, None, 4)
        
        self.assertIsInstance(Driver(None, 12.34, -45.67, "456 High St", None, None, 4), Driver)

        # Test invalid car_capacity input
        with self.assertRaises(TypeError):
            Driver("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, "4")
        
        with self.assertRaises(TypeError):
            Driver("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, None)

    def test_car_capacity_setter(self):
        driver = Driver("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, 4)

        # Test valid input
        driver.car_capacity = 5
        self.assertEqual(driver.car_capacity, 5)

        # Test invalid input
        with self.assertRaises(TypeError):
            driver.car_capacity = "6"

        with self.assertRaises(TypeError):
            driver.car_capacity = None
