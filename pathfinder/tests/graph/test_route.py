import unittest
from lib.graph import Person, Route
from lib.roles import Roles

class Test_route(unittest.TestCase):

    def setUp(self):
        self.person1 = Person("Alice", "555-555-1234", role=Roles.walk)
        self.person2 = Person("Bob", "555-555-5678", role=Roles.passenger)

        self.route1 = Route(self.person1, self.person2, distance=5, duration=10)
        self.route2 = Route(self.person1, self.person2, distance=None, duration=None)

    def test_init(self):
        self.assertEqual(self.route1.origin, self.person1)
        self.assertEqual(self.route1.destination, self.person2)
        self.assertEqual(self.route1.distance, 5)
        self.assertEqual(self.route1.duration, 10)

        self.assertEqual(self.route2.origin, self.person1)
        self.assertEqual(self.route2.destination, self.person2)
        self.assertIsNone(self.route2.distance)
        self.assertIsNone(self.route2.duration)

    def test_invalid_init(self):
        with self.assertRaises(TypeError):
            Route("origin", self.person2, distance=5, duration=10)
        with self.assertRaises(TypeError):
            Route(self.person1, "destination", distance=5, duration=10)
        with self.assertRaises(TypeError):
            Route(self.person1, self.person2, distance="5", duration=10)
        with self.assertRaises(TypeError):
            Route(self.person1, self.person2, distance=5, duration="10")

    def test_set_origin(self):
        self.route1.origin = self.person2
        self.assertEqual(self.route1.origin, self.person2)

    def test_set_invalid_origin(self):
        with self.assertRaises(TypeError):
            self.route1.origin = "origin"

    def test_set_destination(self):
        self.route1.destination = self.person1
        self.assertEqual(self.route1.destination, self.person1)

    def test_set_invalid_destination(self):
        with self.assertRaises(TypeError):
            self.route1.destination = "destination"

    def test_set_distance(self):
        self.route1.distance = 7
        self.assertEqual(self.route1.distance, 7)

    def test_set_invalid_distance(self):
        with self.assertRaises(TypeError):
            self.route1.distance = "7"

    def test_set_duration(self):
        self.route1.duration = 15
        self.assertEqual(self.route1.duration, 15)

    def test_set_invalid_duration(self):
        with self.assertRaises(TypeError):
            self.route1.duration = "15"

    def test_set_none_inputs(self):
        self.route1.distance = None
        self.route1.duration = None

        self.assertIsNone(self.route1.distance)
        self.assertIsNone(self.route1.duration)
