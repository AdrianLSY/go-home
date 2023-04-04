from .utility import Utility
from .person import Person

class Route:
    """
    A class representing a route between an origin and a destination, with optional distance and duration attributes.

    Attributes:
        __origin (Person): The origin of the route, represented by a Person object.
        __destination (Person): The destination of the route, represented by a Person object.
        __distance (float, optional): The distance of the route.
        __duration (float, optional): The duration of the route.

    Raises:
        TypeError if name is not a string / phone is not a string / role is not a Role

    """
    def __init__(self, origin:Person, destination:Person, distance:float = None, duration:float = None):
        Utility.validate_instance_of(origin, Person)
        Utility.validate_instance_of(destination, Person)
        Utility.validate_nullable_instance_of(distance, (int, float))
        Utility.validate_nullable_instance_of(duration, (int, float))
        self.__origin = origin
        self.__destination = destination
        self.__distance = None if distance is None else float(distance)
        self.__duration = None if duration is None else float(duration)

    @property
    def origin(self) -> Person:
        """
        Getter method for the origin attribute.

        Returns:
            Person: The origin location.
        """
        return self.__origin

    @origin.setter
    def origin(self, origin:Person) -> None:
        """
        Setter method for the origin attribute.

        Args:
            origin (str): The new origin.
        
        Raises:
            TypeError: If origin is not a Person
        """
        Utility.validate_instance_of(origin, Person)
        self.__origin = origin

    @property
    def destination(self) -> Person:
        """
        Getter method for the destination attribute.

        Returns:
            Person: The destination location.
        """
        return self.__destination

    @destination.setter
    def destination(self, destination:Person) -> None:
        """
        Setter method for the destination attribute.

        Args:
            destination (str): The new destination.
        
        Raises:
            TypeError: If destination is not a Person
        """
        Utility.validate_instance_of(destination, Person)
        self.__destination = destination

    @property
    def distance(self) -> float:
        """
        Getter method for the distance between two person.

        Returns:
            float: The distance.
        """
        return self.__distance

    @distance.setter
    def distance(self, distance:float) -> None:
        """
        Setter method for the distance attribute.

        Args:
            distance (str): The new distance between two person
        
        Raises:
            TypeError: If distance is not an int or float
        """
        Utility.validate_nullable_instance_of(distance, (int, float))
        self.__distance = None if distance is None else float(distance)

    @property
    def duration(self) -> float:
        """
        Getter method for the duration between two person.

        Returns:
            float: The duration.
        """
        return self.__duration

    @duration.setter
    def duration(self, duration:float) -> None:
        """
        Setter method for the duration attribute.

        Args:
            duration (str): The new duration between two person
        
        Raises:
            TypeError: If duration is not an int or float
        """
        Utility.validate_nullable_instance_of(duration, (int, float))
        self.__duration = None if duration is None else float(duration)
