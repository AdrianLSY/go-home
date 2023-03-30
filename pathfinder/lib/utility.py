class Utility:
    """
    A Collection of utilities and input validations for common tasks

    Functions:
        validate_instance_of(object, a_class) -> None
        validate_nullable_instance_of(object, a_class) -> None
        validate_latitude_and_longitude(latitude:float, longitude:float) -> None
        is_between(number:float, start:float, end:float) -> None
    """
    def validate_instance_of(object, a_class) -> None:
        """
        validates an instance of an object with a class

        Parameters:
        object (any): an instance of a class.
        a_class (any): a class to check against.

        Returns:
        None: if object is an instance of a_class

        Raises:
        TypeError: if the object is not an instance of a_class
        """
        if not isinstance(object, a_class):
            raise TypeError()

    def validate_nullable_instance_of(object, a_class) -> None:
        """
        validates an instance of an object with a class
        Will not perform validations if object is None

        Parameters:
        object (any): an instance of a class.
        a_class (any): a class to check against.

        Returns:
        None: if object is an instance of a_class or None

        Raises:
        TypeError: if the object is not an instance of a_class
        """
        if object is None:
            return
        else:
            Utility.validate_instance_of(object, a_class)

    def validate_latitude_and_longitude(latitude:float, longitude:float) -> None:
        """
        validates latitude and longitudes values to be a float/int and within specified ranges

        Parameters:
        latitude (int, float): the angular distance of a location north or south of the equator (-90 -> 90)
        longitude (int, float): the angular distance of a location east or west of the Prime Meridian (-180 -> 180)

        Returns:
        None: if both latitude and longitude are valid geographic coordinates

        Raises:
        ValueError: if latitude/longitude is not a valid geographic coordinate
        """
        Utility.is_between(latitude, -90, 90)
        Utility.is_between(longitude, -180, 180)

    def is_between(number:float, start:float, end:float) -> None:
        """
        Checks if the given number is between a start and end value.

        Parameters:
        number (float): The number to check.
        start (float): The starting value of the range.
        end (float): The ending value of the range.

        Returns:
        None: if the number is within the range

        Raises:
        ValueError: If number is not between start and end values or start value is greater than the end value
        """
        Utility.validate_instance_of(number, (float, int))
        Utility.validate_instance_of(start, (float, int))
        Utility.validate_instance_of(end, (float, int))

        if start > end:
            raise ValueError("Start value cannot be greater than end value")
        if not start <= number <= end:
            raise ValueError("number is not in range of start and end")
