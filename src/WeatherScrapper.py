from rich.console import Console
from rich.table import Table
from rich import box
import requests
import cord_helper


def main():
    lat, lon, address = cord_helper.locator()

    console = Console()

    url = (f"https://api.weather.gov/points/{lat},{lon}")
    headers = {"User-Agent": "weather-app (ynchenchuh@gmail.com)"}

    with console.status("Fetching weather details...", spinner="dots"):
        data = requests.get(url, headers=headers).json()
        forecast_url = data["properties"]["forecast"]
        forecast = requests.get(forecast_url, headers=headers).json()

    periods = forecast["properties"]["periods"]

    table = Table(box=box.ASCII2, style="green", title=f"[bold]{address}[/bold]")
    table.add_column("Day", justify="center")
    table.add_column("Temp (C)", justify="center")
    table.add_column("Forecast",)

    for i in range(0,len(periods)-1,2):
        day = periods[i]
        night = periods [i+1]

        day_temp = (day["temperature"] -32)*5/9
        night_temp = (night["temperature"]-32)*5/9


        table.add_row(day["name"],f"{round(day_temp,1)} - {round(night_temp,1)}",day["shortForecast"])

    console.clear()
    console.print(table)

if __name__ == "__main__":
    main()