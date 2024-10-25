import datetime

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def process_weather_data(weather_data):
    for entry in weather_data:
        entry['temp'] = kelvin_to_celsius(entry['temp'])
        entry['feels_like'] = kelvin_to_celsius(entry['feels_like'])
    return weather_data

def calculate_daily_aggregates(weather_data):
    avg_temp = sum([entry['temp'] for entry in weather_data]) / len(weather_data)
    max_temp = max([entry['temp'] for entry in weather_data])
    min_temp = min([entry['temp'] for entry in weather_data])
    dominant_condition = max(set([entry['condition'] for entry in weather_data]),
                             key=[entry['condition'] for entry in weather_data].count)
    return {
        'date': datetime.date.today(),
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
