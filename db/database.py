import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Manoj@123",
        database="weather_db"
    )
    return connection

def store_weather_data(weather_data):
    connection = connect_db()
    cursor = connection.cursor()
    for entry in weather_data:
        cursor.execute("""
            INSERT INTO weather_data (city, temperature, feels_like, condition_, time_stamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (entry['city'], entry['temp'], entry['feels_like'], entry['condition_'], entry['time_stamp']))
    connection.commit()
    cursor.close()
    connection.close()

def store_daily_summary(summary):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO daily_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (%s, %s, %s, %s, %s)
    """, (summary['date'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    connection.commit()
    cursor.close()
    connection.close()
