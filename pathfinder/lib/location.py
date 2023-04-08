from enum import Enum
from .utility import Utility

class Location_type(Enum):
    undefined = 0
    start = 1
    end = 2


class Location:
    """
    A class representing a location with an address, latitude, and longitude.

    Attributes:
        __address (str): The address of the location.
        __latitude (float): The latitude of the location.
        __longitude (float): The longitude of the location.
    
    Functions:
        set_address(self, address:str) -> None
        get_address(self) -> str
        set_coordinates(self, latitude:float, longitude:float) -> None
        get_latitude(self) -> float
        get_longitude(self) -> float
    """
    def __init__(self, address:str = None, latitude:float = None, longitude:float = None, type:Location_type = Location_type.undefined) -> None:
        """
        Initializes the Location object that represents a specific geographic location.

        Args:
            address (str, optional): The address of the location.
            latitude (float, optional): The latitude of the location.
            longitude (float, optional): The longitude of the location.
            type (Location_type, optional): undefined location, start/end location of a Person

        Raises:
            TypeError: If the address is not a string or None; if latitude or longitude is not an int, float or None
            ValueError: if latitude/longitude is not a valid geographic coordinate
        """
        Utility.validate_nullable_instance_of(address, str)
        Utility.validate_nullable_latitude_and_longitude(latitude, longitude)
        Utility.validate_instance_of(type, Location_type)
        self.__address = address
        self.__latitude = None if latitude is None else float(latitude)
        self.__longitude = None if longitude is None else float(longitude)
        self.__type = type
    
    @property
    def type(self) -> Location_type:
        """
        Getter method for the location type

        Returns:
            type: The type of location.
        """
        return self.__type

    @type.setter
    def type(self, type:Location_type) -> None:
        """
        Setter method for the location type attribute.

        Args:
            type (Location_type): The new type for the location.
        
        Raises:
            TypeError: If type is not a Location_type
        """
        Utility.validate_nullable_instance_of(type, Location_type)
        self.__type = type
    
    @property
    def address(self) -> str:
        """
        Getter method for the address attribute.

        Returns:
            str: The address of the location.
        """
        return self.__address

    @address.setter
    def address(self, address:str) -> None:
        """
        Setter method for the address attribute.

        Args:
            address (str): The new address for the location.
        
        Raises:
            TypeError: If address is not a string
        """
        Utility.validate_nullable_instance_of(address, str)
        self.__address = address

    @property
    def latitude(self) -> float:
        """
        Getter method for the latitude attribute.

        Returns:
            float: The latitude of the location.
        """
        return self.__latitude

    @property
    def longitude(self) -> float:
        """
        Getter method for the longitude attribute.

        Returns:
            float: The longitude of the location.
        """
        return self.__longitude
    
    def set_coordinates(self, latitude:float, longitude:float) -> None:
        """
        Setter method for the latitude and longitude attributes.

        Args:
            latitude (float): The new latitude for the location.
            longitude (float): The new longitude for the location.
        
        Raises:
            ValueError: If latitude/longitude is not a valid geographic coordinate
            TypeError: If either latitude or longitude is not an int or float
        """
        Utility.validate_nullable_latitude_and_longitude(latitude, longitude)
        self.__latitude = None if latitude is None else float(latitude)
        self.__longitude = None if longitude is None else float(longitude)
