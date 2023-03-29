class Utilities:

    def validate_instance_of(object, a_class):
        if not isinstance(object, a_class):
            raise TypeError()
    
    def validate_nullable_instance_of(self, object, a_class):
        if object is None:
            return
        self.validate_instance_of(object, a_class)
    
    def validate_latitude_and_longitude(self, latitude:float, longitude:float):
        self.is_between(latitude, -90, 90)
        self.is_between(longitude, -180, 180)

    def is_between(self, number:float, start:float, end:float):
        self.validate_instance_of(number, (float, int))
        self.validate_instance_of(start, (float, int))
        self.validate_instance_of(end, (float, int))
    
    def is_between(self, number:float, start:float, end:float):
        self.validate_instance_of(number, (float, int))
        self.validate_instance_of(start, (float, int))
        self.validate_instance_of(end, (float, int))

        if start > end:
            raise ValueError("Start value cannot be greater than end value")
        else:
            return start <= number <= end