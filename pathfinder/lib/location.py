from .utility import Utility

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
    def __init__(self, address:str = None, latitude:float = None, longitude:float = None) -> None:
        """
        Initializes the Location object that represents a specific geographic location.

        Args:
            address (str): The address of the location.
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.

        Raises:
            TypeError: If the address is not a string or None; if latitude or longitude is not an int, float or None
            ValueError: if latitude/longitude is not a valid geographic coordinate
        """
        Utility.validate_nullable_instance_of(address, str)
        Utility.validate_nullable_latitude_and_longitude(latitude, longitude)
        self.__address = address
        self.__latitude = None if latitude is None else float(latitude)
        self.__longitude = None if longitude is None else float(longitude)
    
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
        """
        Utility.validate_instance_of(address, str)
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
        """
        Utility.validate_latitude_and_longitude(latitude, longitude)
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)
