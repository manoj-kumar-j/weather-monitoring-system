def check_threshold(weather_data, threshold):
    alerts = []
    for entry in weather_data:
        if entry['temp'] > threshold:
            alerts.append(f"Alert! {entry['city']} has exceeded {threshold}°C. Current temp: {entry['temp']}°C.")
    return alerts

def trigger_alerts(weather_data, threshold):
    alerts = check_threshold(weather_data, threshold)
    for alert in alerts:
        print(alert)
