import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
# Make sure you have a CSV file named 'weather_data.csv' in the same folder
# The CSV should have columns like: Date, Temperature, Rainfall, Humidity
try:
    df = pd.read_csv("weather_data.csv")
    print("Data loaded successfully.")
except FileNotFoundError:
    print("File not found. Please make sure 'weather_data.csv' exists.")
    exit()

# Step 2: Clean missing values
df = df.dropna()  # remove missing rows

# Convert Date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Extract month for grouping
df['Month'] = df['Date'].dt.month

# Compute monthly averages
monthly_avg = df.groupby('Month').mean(numeric_only=True)
print("\nMonthly Average Data:")
print(monthly_avg)

# Step 3: Create line, bar, and scatter plots in subplots
plt.figure(figsize=(10, 8))

# Line Plot - Average Temperature per Month
plt.subplot(3, 1, 1)
plt.plot(monthly_avg.index, monthly_avg['Temperature'], marker='o')
plt.title('Average Temperature per Month')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Bar Plot - Average Rainfall per Month
plt.subplot(3, 1, 2)
plt.bar(monthly_avg.index, monthly_avg['Rainfall'])
plt.title('Average Rainfall per Month')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')

# Scatter Plot - Temperature vs Humidity
plt.subplot(3, 1, 3)
plt.scatter(df['Temperature'], df['Humidity'], alpha=0.6)
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')

# Adjust layout
plt.tight_layout()

# Step 4: Use NumPy for statistical calculations
temperatures = np.array(df['Temperature'])

mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
std_temp = np.std(temperatures)

print("\nTemperature Statistics:")
print("Mean Temperature:", mean_temp)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Standard Deviation:", std_temp)

# Step 5: Export plots as PNG
plt.savefig("weather_plots.png")
print("\nPlots saved as 'weather_plots.png'.")

# Step 6: Write summary report in Markdown
report = f"""
# Weather Data Visualizer Report

## Overview
This report analyzes local daily weather data to observe climate patterns.

## Monthly Averages
{monthly_avg.to_markdown()}

## Temperature Statistics
- Mean Temperature: {mean_temp:.2f} °C
- Maximum Temperature: {max_temp:.2f} °C
- Minimum Temperature: {min_temp:.2f} °C
- Standard Deviation: {std_temp:.2f} °C

## Insights
1. The line plot shows how temperature changes across months.
2. The bar plot represents average rainfall patterns.
3. The scatter plot shows the relationship between temperature and humidity.

The plots have been exported as 'weather_plots.png' for inclusion in the final sustainability report.
"""

with open("weather_report.md", "w") as f:
    f.write(report)

print("Markdown report 'weather_report.md' created successfully.")
