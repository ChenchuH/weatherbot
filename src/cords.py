from geopy.geocoders import Nominatim

def locator():
    geolocator=Nominatim(user_agent="Weather Bot")
    address = input("Please enter your address: ").strip().lower()

    location = geolocator.geocode(address)

    return location.latitude, location.longitude

def main():
    lat, lon = locator()

if __name__ == "__main__":
    main()
