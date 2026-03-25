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
            if loc_conf in ("y", "yes"):
                return location.latitude, location.longitude, location.address
            elif loc_conf in ("n", "no"):
                continue
            else:
                print("Please print (y/n)")
                continue




def main():
    lat, lon, address = locator()

if __name__ == "__main__":
    main()

