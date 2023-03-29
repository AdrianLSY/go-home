class Utilities:

    def validate_instance_of(object, a_class):
        if not isinstance(object, a_class):
            raise TypeError()
    
    def validate_nullable_instance_of(object, a_class):
        if object is None:
            return
        else:
            Utilities.validate_instance_of(object, a_class)
    
    def validate_latitude_and_longitude(latitude:float, longitude:float):
        Utilities.is_between(latitude, -90, 90)
        Utilities.is_between(longitude, -180, 180)
    
    def is_between(number:float, start:float, end:float):
        Utilities.validate_instance_of(number, (float, int))
        Utilities.validate_instance_of(start, (float, int))
        Utilities.validate_instance_of(end, (float, int))

        if start > end:
            raise ValueError("Start value cannot be greater than end value")
        else:
            return start <= number <= end
