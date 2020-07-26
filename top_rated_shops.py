import googlemaps
from datetime import datetime
import pprint

API_KEY = "AIzaSyA0PEdyIK7EW9uCGm23bEhPF-U7l8fy8wg"
API_KEY = "AIzaSyDre7wyo4C4QUb7g-Htcpb490yI0xw8zkE" #phantompbtraining



gmaps = googlemaps.Client(key=API_KEY)

# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')


# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


coffee_places = gmaps.places(query="coffee", location="Dee Why", radius=1000)

print(coffee_places)

# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# pprint.pprint(directions_result)
