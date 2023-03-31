import googlemaps
from .utility import Utility
from .exception import Api_error, Geocode_exception, Reverse_geocode_exception, API_request_exception, No_route_found_exception, Pair_request_exception

class G_maps_client:
    """
    A class that connects to the Google Maps API and performs operations such as geocoding an address,
    reverse geocoding coordinates, and finding the distance between two addresses.

    Attributes:
        __client: The connected client instance of the Google Maps API.
    """
    def __init__(self, api_key:str) -> None:
        """
        Initializes a new instance of the G_maps_client class.

        Args:
            api_key (str): The API key required to establish a connection with the Google Maps API.

        Attributes:
            client : The connected client instance of the Google Maps API.

        Raises:
            Api_error: If there is an error while establishing a connection with the Google Maps API.
            TypeError: if the api key is not a string

        """
        Utility.validate_instance_of(api_key, str)
        try:
            # establish conenction with the Google Maps API
            self.__client = googlemaps.Client(key=api_key)
        except Api_error as e:
            if e.status_code == 403:
                print("The API key is invalid or has exceeded its quota.")
            else:
                print("There was an error with the Google Maps API.")
    
    def geocode_address(self, address):
        """
        Geocodes the given address and returns its corresponding latitude and longitude values.

        Args:
            address (str): The address to be geocoded.

        Returns:
            dict: A dictionary containing the latitude and longitude values for the given address.

        Raises:
            Geocode_exception: If no results are found for the given address.

        """
        try:
            result = self.client.geocode(address)
            if not result:
                raise Geocode_exception(f"No results found for address: {address}")
            else:
                return result
        except Geocode_exception as e:
            print(f"Error: {e}")

    def reverse_geocode_coordinates(self, latitude, longitude):
        """
        Reverse geocodes the given latitude and longitude values and returns the corresponding human-readable address.

        Args:
            latitude (float): The latitude value of the location to be reverse geocoded.
            longitude (float): The longitude value of the location to be reverse geocoded.

        Returns:
            dict: A dictionary containing the human-readable address for the given latitude and longitude values.

        Raises:
            Reverse_geocode_exception: If no results are found for the given latitude and longitude values.

        """
        try:
            result = self.client.reverse_geocode((latitude, longitude))
            if not result:
                raise Reverse_geocode_exception(f"No results found for coordinates: ({latitude}, {longitude})")
            else:
                return result
        except Reverse_geocode_exception as e:
            print(f"Error: {e}")

    def route_adresses(self, origin:str, destination:str) -> tuple:
        """
        Finds the distance and time taken to travel between the given origin and destination addresses.

        Args:
            origin (str): The starting address of the route.
            destination (str): The ending address of the route.

        Returns:
            tuple: A tuple containing two integers - the distance in meters and the time taken in seconds.

        Raises:
            API_request_exception: If the API request failed.
            Pair_request_exception: If the origin-destination pair request failed.
            No_route_found_exception: If it is impossible to travel between the two locations.

        """
        try:
            result = self.client.distance_matrix(origin, destination)
            if result['status'] != "OK":
                raise API_request_exception(f"API request failed with status: {result['status']}")

            if result['rows'][0]['elements'][0]['status'] == "OK":
               return result['rows'][0]['elements'][0]['distance']['value'], result['rows'][0]['elements'][0]['duration']['value']

            elif result['rows'][0]['elements'][0]['status'] == "ZERO_RESULTS":
               raise No_route_found_exception("It's impossible to travel between the two locations.")

            else:
               raise Pair_request_exception(f"Origin-destination pair request failed with status: {result['rows'][0]['elements'][0]['status']}")

        except API_request_exception as e:
            print(f"Error: {e}")

        except Pair_request_exception as e:
            print(f"Error: {e}")

        except No_route_found_exception as e:
            print(f"Error: {e}")
