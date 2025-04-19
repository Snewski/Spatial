import pandas as pd
from geopy.geocoders import Nominatim 

# Initialize the geocoder
geolocator = Nominatim(user_agent="Spatial_Exam")  # Provide a user-agent string

# Loading dataframe with addresses
data = pd.read_csv("C:/Users/peter/Desktop/Spatial/Exam/Data/places_and_addresses.csv", encoding="WINDOWS-1252")

# Replace "8000 Aarhus Centrum" with "8000 Aarhus"
data['address'] = data['address'].str.replace("8000 Aarhus Centrum", "8000 Aarhus")
# Change address spanning multiple house numbers
data['address'] = data['address'].str.replace("Nørre Allé 24, 26, 8000 Aarhus", "Nørre Allé 24, 8000 Aarhus")

# Geocode each address
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        return pd.Series([location.latitude, location.longitude])
    except:
        return pd.Series([None, None])

data[['latitude', 'longitude']] = data['address'].apply(geocode_address)

# Checking that each address is geocoded
print(data)

# Saving the data 
data.to_csv("C:/Users/peter/Desktop/Spatial/Exam/Data/addresses_with_coordinates.csv", index=False, encoding="WINDOWS-1252")