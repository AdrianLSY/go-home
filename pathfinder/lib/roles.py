from enum import Enum
from .utility import Utility
from .location import Location

class Path():
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None) -> None:
        self.__start_location = Location(start_address, start_latitude, start_longitude)
        self.__end_location = Location(end_address, end_latitude, end_longitude)

    @property
    def start_location(self) -> None:
        return self.__start_location
    
    @start_location.setter
    def start_location(self, location: Location) -> None:
        Utility.validate_instance_of(location, Location)
        self.__start_location = location

    @property
    def end_location(self) -> None:
        return self.__end_location
    
    @end_location.setter
    def end_location(self, location: Location) -> None:
        Utility.validate_instance_of(location, Location)
        self.__end_location = location

class Walk(Path):
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None) -> None:
        super().__init__(start_address, start_latitude, start_longitude, end_address, end_latitude, end_longitude)


class Passenger(Path):
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None) -> None:
        super().__init__(start_address, start_latitude, start_longitude, end_address, end_latitude, end_longitude)


class Driver(Path):
    def __init__(self, start_address:str = None, start_latitude:float = None, start_longitude:float = None, end_address:str = None, end_latitude:float = None, end_longitude:float = None, car_capacity:int = 0) -> None:
        super().__init__(start_address, start_latitude, start_longitude, end_address, end_latitude, end_longitude)
        Utility.validate_instance_of(car_capacity, int)
        self.__car_capacity = car_capacity

    @property
    def car_capacity(self) -> None:
        return self.__car_capacity

    @car_capacity.setter
    def car_capacity(self, car_capacity:int) -> int:
        Utility.validate_instance_of(car_capacity, int)
        self.__car_capacity = car_capacity


class Roles(Enum):
    walk = Walk()
    driver = Driver()
    passenger = Passenger()