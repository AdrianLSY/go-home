from enum import Enum
from .utilities import Utilities
from .location import Location
from .roles import Roles

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
    def __init__(self, origin:Person, destination:Person, distance:int = None, duration:int = None):
        Utilities.validate_instance_of(origin, Person)
        Utilities.validate_instance_of(destination, Person)
        Utilities.validate_nullable_instance_of(distance, int)
        Utilities.validate_nullable_instance_of(duration, int)
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.duration = duration
