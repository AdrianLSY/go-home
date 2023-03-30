from enum import Enum
from .utility import Utility
from .location import Location
from .roles import Roles

class Person:
    def __init__(self, name:str, phone:str, home_location:Location, role:Roles = Roles) -> None:
        Utility.validate_instance_of(name, str)
        Utility.validate_instance_of(phone, str)
        Utility.validate_instance_of(home_location, Location)
        Utility.validate_instance_of(role, Roles)
        self.name = name
        self.phone = phone
        self.home_location = home_location
        self.role = role


class Path:
    def __init__(self, origin:Person, destination:Person, distance:int = None, duration:int = None):
        Utility.validate_instance_of(origin, Person)
        Utility.validate_instance_of(destination, Person)
        Utility.validate_nullable_instance_of(distance, int)
        Utility.validate_nullable_instance_of(duration, int)
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.duration = duration
