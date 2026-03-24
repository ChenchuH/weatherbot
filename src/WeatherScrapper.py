import requests

url = "https://api.weather.gov/points/33.83,-118.34"

headers = {
    "User-Agent": "weather-app (youremail@example.com)"
}

# get forecast URL
data = requests.get(url, headers=headers).json()
forecast_url = data["properties"]["forecast"]

# get forecast data
forecast = requests.get(forecast_url, headers=headers).json()

# print each day
for p in forecast["properties"]["periods"]:
    print(p["name"], "-", p["temperature"], p["temperatureUnit"])