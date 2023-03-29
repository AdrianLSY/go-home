from googlemaps.exceptions import ApiError as Api_error

class API_request_exception(Exception):
    pass

class Pair_request_exception(Exception):
    pass

class No_route_found_exception(Exception):
    pass

class Geocode_exception(Exception):
    pass

class Reverse_geocode_exception(Exception):
    pass

class Invalid_latitude_exception(Exception):
    pass

class Invalid_longitude_exception(Exception):
    pass
