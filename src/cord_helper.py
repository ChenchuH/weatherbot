from geopy.geocoders import Nominatim

def locator():
    geolocator=Nominatim(user_agent="Weather Bot")

    while True:
        address = input("Please enter your address: ").strip().lower()
        location = geolocator.geocode(address)

        if location is None:
            print("No Location found, please try again: ")
        else:
            loc_conf=input(f"Is this your addresss (y/n) {location.address}: ").lower()
            if loc_conf == "y":
                return location.latitude, location.longitude
            else:
                continue

def main():
    lat, lon = locator()

if __name__ == "__main__":
    main()
