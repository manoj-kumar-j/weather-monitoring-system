import matplotlib.pyplot as plt

def plot_temperature_trend(daily_data):
    dates = [entry['date'] for entry in daily_data]
    temps = [entry['avg_temp'] for entry in daily_data]
    
    plt.plot(dates, temps, marker='o')
    plt.title("Daily Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    plt.show()
