# Real-Time Weather Monitoring System

This project is a real-time weather monitoring system that retrieves, processes, and visualizes weather data from the OpenWeatherMap API for major Indian metros. It includes daily summaries, alerting thresholds, and visualization capabilities.

---

## Table of Contents

1. [Features](#features)
2. [Design Choices](#design-choices)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
5. [Setup and Configuration](#setup-and-configuration)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Future Improvements](#future-improvements)

---

### Features

- Real-time weather data retrieval
- Daily weather summaries with rollups and aggregates
- Customizable alert thresholds
- Data visualization for historical trends and alerts

### Design Choices

- **Architecture**: The project is modular with separate modules for data retrieval, processing, and storage, allowing easy updates and scalability.
- **Database**: MySQL is used for persistent storage of weather data summaries.
- **Alert System**: Console-based alerts with potential to expand to email notifications.
- **Visualization**: Matplotlib is used to visualize daily summaries and historical trends.

---

### Dependencies

The project dependencies are listed in `requirements.txt`. Key dependencies include:

- `requests`: To fetch data from the OpenWeatherMap API.
- `mysql-connector-python`: To connect and interact with a MySQL database.
- `matplotlib`: To generate visualizations of weather data trends.

Additional dependencies are as follows:

- Python 3.8+ (recommended)
- MySQL (database server)

---

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/weather-monitoring-system.git
   cd weather-monitoring-system
