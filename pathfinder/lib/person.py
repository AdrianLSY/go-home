from .utility import Utility
from .roles import Roles

class Person:
    """
    A class representing a person with a name, phone number, and role in the transportation system.

    Attributes:
        __name (str): The name of the person.
        __phone (str): The phone number of the person.
        __role (Roles): The role of the person in the transportation system.

    Raises:
        TypeError if name is not a string / phone is not a string / role is not a Role
    """
    def __init__(self, name:str, phone:str, role:Roles = Roles) -> None:
        Utility.validate_instance_of(name, str)
        Utility.validate_instance_of(phone, str)
        Utility.validate_instance_of(role, Roles)
        self.__name = name
        self.__phone = phone
        self.__role = role

    @property
    def name(self) -> str:
        """
        Getter method for the name attribute.

        Returns:
            str: The name of the person.
        """
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        """
        Setter method for the name attribute.

        Args:
            name (str): The new name for the Person.
        
        Raises:
            TypeError: If name is not a string
        """
        Utility.validate_instance_of(name, str)
        self.__name = name

    @property
    def phone(self) -> str:
        """
        Getter method for the phone attribute.

        Returns:
            str: The phone number of the person.
        """
        return self.__phone

    @phone.setter
    def phone(self, phone:str) -> None:
        """
        Setter method for the phone attribute.

        Args:
            phone (str): The new phone number for the location.
        
        Raises:
            TypeError: If phone is not a string
        """
        Utility.validate_instance_of(phone, str)
        self.__phone = phone

    @property
    def role(self) -> Roles:
        """
        Getter method for the role attribute.

        Returns:
            Roles: The role of the location.
        """
        return self.__role

    @role.setter
    def role(self, role:Roles) -> None:
        """
        Setter method for the role attribute.

        Args:
            role (str): The new role
        
        Raises:
            TypeError: If role is not a Role
        """
        Utility.validate_instance_of(role, Roles)
        self.__role = role
