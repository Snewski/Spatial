import pandas as pd
from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="Spatial_Exam")

# Load the dataframe with latitude and longitude
data = pd.read_csv("Data/places_with_coordinates.csv", encoding="WINDOWS-1252")

# Reverse geocode each coordinate pair
def reverse_geocode(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        return location.address if location else None
    except:
        return None

# Apply reverse geocoding
data['address'] = data.apply(lambda row: reverse_geocode(row['latitude'], row['longitude']), axis=1)

# Checking results
print(data)

# Save the updated data
data.to_csv("Data/addresses_with_coordinates.csv", index=False, encoding="WINDOWS-1252")