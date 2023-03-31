from enum import Enum
from .utility import Utility
from .location import Location

class Path():
    """
    Represents a path from a start location to an end location.

    Attributes:
        __start_location (Location): Start location of the path.
        __end_location (Location): End location of the path.
    """
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None) -> None:
        """
        Initializes the Path object with start and end locations.

        Parameters:
            start_address (str): Start address of the path.
            start_latitude (float): Start latitude of the path.
            start_longitude (float): Start longitude of the path.
            end_address (str): End address of the path.
            end_latitude (float): End latitude of the path.
            end_longitude (float): End longitude of the path.
        """
        self.__start_location = Location(start_address, start_latitude, start_longitude)
        self.__end_location = Location(end_address, end_latitude, end_longitude)

    @property
    def start_location(self) -> Location:
        """
        Gets the start location of the path.

        Returns:
            Location: Start location of the path.
        """
        return self.__start_location
    
    @start_location.setter
    def start_location(self, location: Location) -> None:
        """
        Sets the start location of the path.
    
        Parameters:
            location (Location): New start location.
        
        Returns:
            None
    
        Raises:
            TypeError: If the location is not an instance of Location.
        """
        Utility.validate_instance_of(location, Location)
        self.__start_location = location

    @property
    def end_location(self) -> Location:
        """
        Gets the end location of the path.

        Returns:
            Location: Etart location of the path.
        """
        return self.__end_location
    
    @end_location.setter
    def end_location(self, location: Location) -> None:
        """
        Sets the end location of the path.
    
        Parameters:
            location (Location): New end location.
        
        Returns:
            None
    
        Raises:
            TypeError: If the location is not an instance of Location.
        """
        Utility.validate_instance_of(location, Location)
        self.__end_location = location

class Walk(Path):
    """
    A class representing a path for a person walking.
    """
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None) -> None:
        super().__init__(start_address, start_latitude, start_longitude, end_address, end_latitude, end_longitude)


class Passenger(Path):
    """
    A class representing a path for a person riding as a passenger in a Driver's car.
    """
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None) -> None:
        super().__init__(start_address, start_latitude, start_longitude, end_address, end_latitude, end_longitude)


class Driver(Path):
    """
    A class representing a path for a person driving while having passengers in their car.
    """
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None, car_capacity:int = 0) -> None:
        super().__init__(start_address, start_latitude, start_longitude, end_address, end_latitude, end_longitude)
        Utility.validate_instance_of(car_capacity, int)
        self.__car_capacity = car_capacity

    @property
    def car_capacity(self) -> int:
        """Get the capacity of the car.

        Returns:
            int: The capacity of the car.
        """
        return self.__car_capacity

    @car_capacity.setter
    def car_capacity(self, car_capacity:int) -> int:
        """Set the capacity of the car.

        Args:
            car_capacity (int): The capacity of the car.

        Raises:
            TypeError: If car_capacity is not an integer.

        Returns:
            None
        """
        Utility.validate_instance_of(car_capacity, int)
        self.__car_capacity = car_capacity


class Roles(Enum):
    walk = Walk()
    driver = Driver()
    passenger = Passenger()
