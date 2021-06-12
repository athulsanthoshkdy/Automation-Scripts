import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        print(f"Weather in {city}: {temp:.2f}°C")
    else:
        print(f"Error fetching weather: {data['message']}")

get_weather("New York")
