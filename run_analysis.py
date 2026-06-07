import pandas as pd
import kagglehub
import matplotlib.pyplot as plt
import os

print(" 1. Downloading and loading the dataset from Kaggle...")
#Automatically fetch the dataset

path = kagglehub.dataset_download("usdot/flight-delays")
flights_file = os.path.join(path, "flights.csv")
#Load the dataset while selecting only the essential columns to optimize performance and minimize memory consumption.

columns_to_keep = ['YEAR', 'MONTH', 'DAY', 'AIRLINE', 'FLIGHT_NUMBER', 'DEPARTURE_DELAY', 'ARRIVAL_DELAY']
flights = pd.read_csv(flights_file, usecols=columns_to_keep)

print("🧹 2. Cleaning data (Handling missing values)...")
#Data cleaning: drop rows with missing values in the delay time fields

flights_cleaned = flights.dropna(subset=['DEPARTURE_DELAY', 'ARRIVAL_DELAY'])

print("\n📊 3. Executive Summary (Insights for Recruiters):")
print("-" * 50)
total_flights = len(flights_cleaned)
print(f"Total Flights Analyzed: {total_flights:,}")

#First Analysis: Average departure delay by airline

print("\n✈️ Average Departure Delay by Airline (Top 5):")
airline_delays = flights_cleaned.groupby('AIRLINE')['DEPARTURE_DELAY'].mean().sort_values(ascending=False).head(5)
print(airline_delays)

#Second Analysis: Identifying the months with the highest frequency of flight delays

print("\n📅 Average Departure Delay by Month:")
monthly_delays = flights_cleaned.groupby('MONTH')['DEPARTURE_DELAY'].mean()
print(monthly_delays)
#Generate a professional visualization of the average airline delays
print("\n🎨 4. Generating Professional Visualization...")
plt.figure(figsize=(10, 6))
airline_all_delays = flights_cleaned.groupby('AIRLINE')['DEPARTURE_DELAY'].mean().sort_values(ascending=False)
airline_all_delays.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Flight Departure Delay by Airline', fontsize=14, fontweight='bold')
plt.xlabel('Airline Code', fontsize=12)
plt.ylabel('Average Delay (Minutes)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

#Export the plot as an image and store it in the project directory for uploading to GitHub
chart_path = 'airline_delay_analysis.png'
plt.savefig(chart_path)
print(f"Success! Visual chart saved as '{chart_path}'")