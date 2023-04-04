import unittest
from lib.roles import Walk

class Test_walk(unittest.TestCase):

    def test_init(self):
        # Test valid input
        walk = Walk("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90)
        self.assertEqual(walk.start_location.address, "123 Main St")
        self.assertEqual(walk.start_location.latitude, 12.34)
        self.assertEqual(walk.start_location.longitude, -45.67)
        self.assertEqual(walk.end_location.address, "456 High St")
        self.assertEqual(walk.end_location.latitude, 34.56)
        self.assertEqual(walk.end_location.longitude, -78.90)

        # Test empty input
        walk2 = Walk()
        self.assertIsNone(walk2.start_location.address)
        self.assertIsNone(walk2.start_location.latitude)
        self.assertIsNone(walk2.start_location.longitude)
        self.assertIsNone(walk2.end_location.address)
        self.assertIsNone(walk2.end_location.latitude)
        self.assertIsNone(walk2.end_location.longitude)

        # Test partial input
        self.assertIsInstance(Walk(None, 12.34, -45.67, "456 High St", 34.56, -78.90), Walk)

        with self.assertRaises(TypeError):
            Walk("123 Main St", None, -45.67, "456 High St", 34.56, -78.90)

        with self.assertRaises(TypeError):
            Walk("123 Main St", 12.34, None, "456 High St", 34.56, -78.90)
        
        self.assertIsInstance(Walk("123 Main St", None, None, "456 High St", 34.56, -78.90), Walk)

        self.assertIsInstance(Walk("123 Main St", 12.34, -45.67, None, 34.56, -78.90), Walk)

        with self.assertRaises(TypeError):
            Walk("123 Main St", 12.34, -45.67, "456 High St", None, -78.90)

        with self.assertRaises(TypeError):
            Walk("123 Main St", 12.34, -45.67, "456 High St", 34.56, None)
        
        self.assertIsInstance(Walk(None, 12.34, -45.67, "456 High St", None, None), Walk)

        # Test invalid car_capacity input
        with self.assertRaises(TypeError):
            Walk("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, "4")
        
        with self.assertRaises(TypeError):
            Walk("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90, None)
