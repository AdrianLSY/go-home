from enum import Enum
from utilities import Utilities

class Location:
    
    def __init__(self, address:str, latitude:float = None, longitude:float = None) -> None:
        Utilities.validate_instance_of(address, str)
        Utilities.validate_latitude_and_longitude(latitude, longitude)
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class Walk:
    pass


class Driver:
    def __init__(self, car_capacity:int = None, start_location:Location = None) -> None:
        Utilities.validate_instance_of(car_capacity, int)
        Utilities.validate_instance_of(start_location, Location)
        if car_capacity < 0:
            raise ValueError("Car cannot have a negative number")
        self.car_capacity = car_capacity
        self.start_location = start_location


class Passenger:
    def __init__(self, start_location:Location = None) -> None:
        Utilities.validate_instance_of(start_location, Location)
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


class Person:
    def __init__(self, name:str, phone:str, home_location:Location, role:Roles = Roles) -> None:
        Utilities.validate_instance_of(name, str)
        Utilities.validate_instance_of(phone, str)
        Utilities.validate_instance_of(home_location, Location)
        Utilities.validate_instance_of(role, Roles)
        self.name = name
        self.phone = phone
        self.home_location = home_location
        self.role = role


class Path:
    def __init__(self, person_1:Person, person_2:Person, distance:int = None, duration:int = None):
        Utilities.validate_instance_of(person_1, Person)
        Utilities.validate_instance_of(person_2, Person)
        Utilities.validate_nullable_instance_of(distance, int)
        Utilities.validate_nullable_instance_of(duration, int)
        self.person_1 = person_1
        self.person_2 = person_2
        self.distance = distance
        self.duration = duration


if __name__ == '__main__':
    walker = Roles.walk
    print(walker.value)
