from enum import Enum

class Location:
    def __init__(self, address:str, latitude:int = None, longitude:int = None):
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
    
    def validate_latitude_and_longitude(latitude, longitude):
        # Check if latitude or longitude is None
        if latitude is None or longitude is None:
            return False

        # Check if the latitude is within its valid range
        if latitude < -90 or latitude > 90:
            return False

        # Check if the longitude is within its valid range
        if longitude < -180 or longitude > 180:
            return False

        # If both checks pass, the coordinates are valid
        return True


class Walk:
    pass


class Driver:
    def __init__(self, car_capacity:int = None, start_location:Location = None) -> None:
        self.car_capacity = car_capacity
        self.start_location = start_location


class Passenger:
    def __init__(self, start_location:Location = None) -> None:
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
    def __init__(self, name:str, phone:str, home_location:Location, role:Roles = Roles.walk) -> None:
        self.name = name
        self.phone = phone
        self.home_location = home_location


class Path:
    def __init__(self, person_1:Person, person_2:Person, distance = None, duration = None):
        self.person_1 = person_1
        self.person_2 = person_2
        self.distance = distance
        self.duration = duration


if __name__ == '__main__':
    walker = Roles.walk
    print(walker.value)
