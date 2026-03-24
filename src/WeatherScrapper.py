from rich.console import Console
from rich.table import Table
import requests

console = Console()

url = "https://api.weather.gov/points/33.83,-118.34"
headers = {"User-Agent": "weather-app (ynchenchuh@gmail.com)"}

data = requests.get(url, headers=headers).json()
forecast_url = data["properties"]["forecast"]
forecast = requests.get(forecast_url, headers=headers).json()

table = Table(title="Weather Forecast")
table.add_column("Day", style="bold")
table.add_column("Temp (C)", justify="center")
table.add_column("Forecast")

for f in forecast["properties"]["periods"]:
    c_temp = (f["temperature"] - 32) * 5 / 9
    table.add_row(f["name"],f"{round(c_temp,1)}",f["shortForecast"])

console.print(table)