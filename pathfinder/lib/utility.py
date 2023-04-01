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
        Validates if an object is a direct instance of a_class or any class in a tuple of classes

        Parameters:
            object (any): An instance of a class.
            a_class (any): A class or a tuple of classes to check against.

        Returns:
            None: If the object is a direct instance of a_class or any class in a tuple of classes

        Raises:
            TypeError: If the object is not a direct instance of a_class or any class in a tuple of classes
        """
        if not isinstance(a_class, tuple):
            a_class = (a_class,)
            
        if not type(object) in a_class:
            raise TypeError()

    def validate_nullable_instance_of(object, a_class) -> None:
        """
        Validates an instance of an object with a class
        Will not perform validations if object is None

        Parameters:
            object (any): An instance of a class.
            a_class (any): A class to check against.

        Returns:
            None: If object is an instance of a_class or None

        Raises:
            TypeError: If the object is not an instance of a_class
        """
        if object is None:
            return
        else:
            Utility.validate_instance_of(object, a_class)

    def validate_latitude_and_longitude(latitude:float, longitude:float) -> None:
        """
        Validates latitude and longitudes values to be a float/int and within specified ranges

        Parameters:
            latitude (int, float): The angular distance of a location north or south of the equator (-90 -> 90)
            ongitude (int, float): The angular distance of a location east or west of the Prime Meridian (-180 -> 180)

        Returns:
            None: If both latitude and longitude are valid geographic coordinates

        Raises:
            ValueError: If latitude/longitude is not a valid geographic coordinate
            TypeError: If either latitude or longitude is not an int or float
        """
        Utility.is_between(latitude, -90, 90)
        Utility.is_between(longitude, -180, 180)

    def validate_nullable_latitude_and_longitude(latitude:float, longitude:float) -> None:
        """
        Validates latitude and longitudes values to be a float/int and within specified ranges

        Parameters:
            latitude (int, float): The angular distance of a location north or south of the equator (-90 -> 90)
            longitude (int, float): The angular distance of a location east or west of the Prime Meridian (-180 -> 180)

        Returns:
            None: If both latitude and longitude are valid geographic coordinates or None

        Raises:
            ValueError: If latitude/longitude is not a valid geographic coordinate
            TypeError: If either latitude or longitude is not an int or float
        """
        if latitude is None and longitude is None:
            return
        else:
            Utility.validate_latitude_and_longitude(latitude, longitude)

    def is_between(number:float, start:float, end:float) -> None:
        """
        Checks if the given number is between a start and end value.

        Parameters:
            number (float): The number to check.
            start (float): The starting value of the range.
            end (float): The ending value of the range.

        Returns:
            None: If the number is within the range

        Raises:
            ValueError: If number is not between start and end values or start value is greater than the end value
            TypeError: If number, start or end is not a float or an int
        """
        Utility.validate_instance_of(number, (float, int))
        Utility.validate_instance_of(start, (float, int))
        Utility.validate_instance_of(end, (float, int))

        if start > end:
            raise ValueError("Start value cannot be greater than end value")
        if not start <= number <= end:
            raise ValueError("Number is not in range of start and end")
    
    def check_bigger(number:float, threshold:float) -> None:
        """
        Checks if the given number is bigger than a given threshold.

        Args:
            number (float or int): The number to be checked.
            threshold (float or int): The reference number to compare against.

        Returns:
            None: If the number is bigger than the threshold.

        Raises:
            ValueError: If the number is not bigger than the threshold.
            TypeError: If either number or threshold is not a float or int.
        """
        Utility.validate_instance_of(number, (int, float))
        Utility.validate_instance_of(threshold, (int, float))

        if number > threshold:
            return None
        else:
            raise ValueError(f"{number} is not bigger than {threshold}")


    def check_smaller(number, threshold):
        """
        Checks if the given number is smaller than a given threshold.

        Args:
            number (float or int): The number to be checked.
            threshold (float or int): The reference number to compare against.

        Returns:
            None: If the number is smaller than the threshold.

        Raises:
            ValueError: If the number is not smaller than the threshold.
            TypeError: If either number or threshold is not a float or int.
        """
        Utility.validate_instance_of(number, (int, float))
        Utility.validate_instance_of(threshold, (int, float))

        if number < threshold:
            return None
        else:
            raise ValueError(f"{number} is not smaller than {threshold}")
