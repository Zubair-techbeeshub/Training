import requests
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
def get_coordinates(city):
    try:
        response = requests.get(GEOCODE_URL,
            params={
                "name": city,
                "count": 1
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        if "results" not in data:
            return None
        location = data["results"][0]
        return (
            location["latitude"],
            location["longitude"],
            location["name"],
            location["country"]
        )

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def get_weather(latitude, longitude):
    try:
        response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m"
                ]
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def display_weather(location, weather):
    current = weather["current"]
    print("\nCurrent Weather")
    print("-" * 40)
    print(f"City        : {location[2]}")
    print(f"Country     : {location[3]}")
    print(f"Temperature : {current['temperature_2m']} °C")
    print(f"Humidity    : {current['relative_humidity_2m']} %")
    print(f"Wind Speed  : {current['wind_speed_10m']} km/h")
    print("-" * 40)

def main():
    city = input("Enter city name: ")
    location = get_coordinates(city)
    if location is None:
        print("City not found.")
        return
    weather = get_weather(location[0], location[1])
    if weather:
        display_weather(location, weather)

if __name__ == "__main__":
    main()
