from enum import Enum
from .utilities import Utilities
from .location import Location

class Walk:
    pass


class Driver:
    def __init__(self, car_capacity:int = None, start_location:Location = None) -> None:
        Utilities.validate_nullable_instance_of(car_capacity, int)
        Utilities.validate_nullable_instance_of(start_location, Location)
        self.car_capacity = car_capacity
        self.start_location = start_location


class Passenger:
    def __init__(self, start_location:Location = None) -> None:
        Utilities.validate_nullable_instance_of(start_location, Location)
        self.start_location = start_location


class Roles(Enum):
    """
    # Used to declare a User (person) role

    WALK: Exclude them from being assigned to anything
    DRIVER: Assign Passangers to them
    PASSANGER

    """
    walk = Walk()
    driver = Driver()
    passenger = Passenger()