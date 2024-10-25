from fetcher.weather_fetcher import fetch_all_cities
from processor.data_processor import process_weather_data, calculate_daily_aggregates
from db.database import store_weather_data, store_daily_summary
from alert.alerting_system import trigger_alerts
from visualize.visualization import plot_temperature_trend

def main():
    # Fetch real-time weather data
    weather_data = fetch_all_cities()

    # Process and store the weather data
    processed_data = process_weather_data(weather_data)
    store_weather_data(processed_data)

    # Calculate and store daily summary
    daily_summary = calculate_daily_aggregates(processed_data)
    store_daily_summary(daily_summary)

    # Trigger alerts if temperature exceeds threshold
    trigger_alerts(processed_data, threshold=35)

    # Visualize daily temperature trend
    plot_temperature_trend([daily_summary])  # For simplicity, only one day is passed

if __name__ == "__main__":
    main()
