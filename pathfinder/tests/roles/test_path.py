import unittest
from lib.location import Location
from lib.roles import Path

class TestPath(unittest.TestCase):

    def test_init(self):
        # Test valid input
        path = Path("123 Main St", 12.34, -45.67, "456 High St", 34.56, -78.90)
        self.assertEqual(path.start_location.address, "123 Main St")
        self.assertEqual(path.start_location.latitude, 12.34)
        self.assertEqual(path.start_location.longitude, -45.67)
        self.assertEqual(path.end_location.address, "456 High St")
        self.assertEqual(path.end_location.latitude, 34.56)
        self.assertEqual(path.end_location.longitude, -78.90)

        # Test empty input
        path2 = Path()
        self.assertIsNone(path2.start_location.address)
        self.assertIsNone(path2.start_location.latitude)
        self.assertIsNone(path2.start_location.longitude)
        self.assertIsNone(path2.end_location.address)
        self.assertIsNone(path2.end_location.latitude)
        self.assertIsNone(path2.end_location.longitude)

        # Test invalid input types
        with self.assertRaises(TypeError):
            Path(123, 12.34, -45.67, "456 High St", 34.56, -78.90)

        with self.assertRaises(TypeError):
            Path("123 Main St", "12.34", -45.67, "456 High St", 34.56, -78.90)

        with self.assertRaises(TypeError):
            Path("123 Main St", 12.34, "-45.67", "456 High St", 34.56, -78.90)

        # Test invalid coordinates
        with self.assertRaises(ValueError):
            Path("123 Main St", 91, -45.67, "456 High St", 34.56, -78.90)

        with self.assertRaises(ValueError):
            Path("123 Main St", 12.34, -181, "456 High St", 34.56, -78.90)
        
        # Test partial input
        self.assertIsInstance(Path(None, 12.34, -45.67, "456 High St", 34.56, -78.90), Path)

        with self.assertRaises(TypeError):
            Path("123 Main St", None, -45.67, "456 High St", 34.56, -78.90)

        with self.assertRaises(TypeError):
            Path("123 Main St", 12.34, None, "456 High St", 34.56, -78.90)
        
        self.assertIsInstance(Path("123 Main St", None, None, "456 High St", 34.56, -78.90), Path)

        self.assertIsInstance(Path("123 Main St", 12.34, -45.67, None, 34.56, -78.90), Path)

        with self.assertRaises(TypeError):
            Path("123 Main St", 12.34, -45.67, "456 High St", None, -78.90)

        with self.assertRaises(TypeError):
            Path("123 Main St", 12.34, -45.67, "456 High St", 34.56, None)
        
        self.assertIsInstance(Path("123 Main St", 12.34, -45.67, "456 High St", None, None), Path)

    def test_start_location_setter(self):
        path = Path()

        # Test valid input
        start_location = Location("789 State St", 56.78, -90.12)
        path.start_location = start_location
        self.assertEqual(path.start_location.address, "789 State St")
        self.assertEqual(path.start_location.latitude, 56.78)
        self.assertEqual(path.start_location.longitude, -90.12)

        # Test invalid input
        with self.assertRaises(TypeError):
            path.start_location = "Invalid input"

        # Test None input
        path.start_location = None
        self.assertEqual(path.start_location, None)

    def test_end_location_setter(self):
        path = Path()

        # Test valid input
        end_location = Location("1011 Central Blvd", 78.90, -123.45)
        path.end_location = end_location
        self.assertEqual(path.end_location.address, "1011 Central Blvd")
        self.assertEqual(path.end_location.latitude, 78.90)
        self.assertEqual(path.end_location.longitude, -123.45)

        # Test invalid input
        with self.assertRaises(TypeError):
            path.end_location = "Invalid input"

        # Test None input
        path.start_location = None
        self.assertEqual(path.start_location, None)
