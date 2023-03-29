from .utilities import Utilities

class Location:
    
    def __init__(self, address:str, latitude:float = None, longitude:float = None) -> None:
        Utilities.validate_instance_of(address, str)
        Utilities.validate_latitude_and_longitude(latitude, longitude)
        self.address = address
        self.latitude = float(latitude)
        self.longitude = float(longitude)