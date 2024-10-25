import requests

API_KEY = "95ae115397906d6e479e9dfd2eaea3a5"  # Replace with your API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'condition_': data['weather'][0]['main'],
            'time_stamp': data['dt']
        }
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

def fetch_all_cities():
    weather_data = []
    for city in CITIES:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)
    return weather_data
