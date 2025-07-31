import pandas as pd
from datetime import datetime

# Initialize data structures
weather_data = []
unique_dates = set()

# Function to validate date
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to add weather data
def add_weather_data():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format! Use YYYY-MM-DD.")
        return
    
    if date in unique_dates:
        print("Data for this date already exists!")
        return
    
    try:
        temperature = float(input("Enter temperature (°C): "))
    except ValueError:
        print("Invalid temperature value!")
        return
    
    condition = input("Enter weather condition (Sunny/Rainy/Cloudy etc.): ")
    
    weather_data.append({"Date": date, "Temperature": temperature, "Condition": condition})
    unique_dates.add(date)
    print("✅ Data added successfully.")

# Function to view all data
def view_data():
    if not weather_data:
        print("No weather data recorded yet.")
        return
    df = pd.DataFrame(weather_data)
    print("\n--- Weather Data ---")
    print(df)

# Function to summarize trends
def summarize_data():
    if not weather_data:
        print("No data available for summary.")
        return
    df = pd.DataFrame(weather_data)
    avg_temp = df["Temperature"].mean()
    print(f"\n🌡 Average Temperature: {avg_temp:.2f}°C")

# Function to export data to CSV
def export_to_csv():
    if not weather_data:
        print("No data available to export.")
        return
    df = pd.DataFrame(weather_data)
    df.to_csv("weather_data.csv", index=False)
    print("✅ Data exported to weather_data.csv successfully.")

# Main menu
while True:
    print("\n--- Weather Data Recorder ---")
    print("1. Add Weather Data")
    print("2. View Weather Data")
    print("3. Summarize Trends")
    print("4. Export to CSV")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_weather_data()
    elif choice == '2':
        view_data()
    elif choice == '3':
        summarize_data()
    elif choice == '4':
        export_to_csv()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")