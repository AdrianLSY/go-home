import googlemaps
from .utilities import Utilities
from .exceptions import Api_error, Geocode_exception, Reverse_geocode_exception, API_request_exception, No_route_found_exception, Pair_request_exception

class G_maps_client:

    def __init__(self, api_key:str) -> None:
        Utilities.validate_instance_of(api_key, str)
        try:
             # establish conenction with the Google Maps API
            self.client = googlemaps.Client(key=api_key)
        except Api_error as e:
            if e.status_code == 403:
                print("The API key is invalid or has exceeded its quota.")
            else:
                print("There was an error with the Google Maps API.")

    def geocode_address(self, address):
        try:
            result = self.client.geocode(address)
            if not result:
                raise Geocode_exception(f"No results found for address: {address}")
            else:
                return result
        except Geocode_exception as e:
            print(f"Error: {e}")

    def reverse_geocode_coordinates(self, latitude, longitude):
        try:
            result = self.client.reverse_geocode((latitude, longitude))
            if not result:
                raise Reverse_geocode_exception(f"No results found for coordinates: ({latitude}, {longitude})")
            else:
                return result
        except Reverse_geocode_exception as e:
            print(f"Error: {e}")

    def route_adresses(self, origin:str, destination:str) -> tuple:
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