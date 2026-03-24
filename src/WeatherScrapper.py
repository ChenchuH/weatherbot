import requests

url = "https://api.weather.gov/points/33.83,-118.34"

headers = {"User-Agent": "weather-app (ynchenchuh@gmail.com)"}

# get forecast URL
data = requests.get(url, headers=headers).json()
forecast_url = data["properties"]["forecast"]

# get forecast data
forecast = requests.get(forecast_url, headers=headers).json()

# print each day
for f in forecast["properties"]["periods"]:
    f_temp = f["temperature"]
    c_temp = (f_temp-32)*(5/9)

    print(f["name"], "-", round(c_temp,1), "C")