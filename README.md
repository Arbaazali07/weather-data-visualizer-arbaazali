# weather-data-visualizer-arbaazali

## Project Title
Weather Data Visualizer – Python-Based Weather Analysis and Visualization Tool

## Course
Programming for Problem Solving using Python

## Objective
This project analyzes real-world weather data and presents meaningful insights through statistics and visualizations. It demonstrates Python skills in:

- Data loading and cleaning using Pandas
- Numerical computations and statistics with NumPy
- Visualizations with Matplotlib
- Grouping, aggregation, and trend analysis
- Exporting cleaned data and summary reports

## Dataset
The dataset is a **daily weather dataset** for one year (2024) with the following columns:

| Column      | Description                     |
|------------|---------------------------------|
| date       | Calendar date (YYYY-MM-DD)      |
| temperature| Average daily temperature (°C)  |
| humidity   | Average daily humidity (%)      |
| rainfall   | Daily rainfall (mm)             |

Files included:

## Tools and Libraries
- Python 3.x
- Pandas
- NumPy
- Matplotlib

## Project Workflow

1. **Data Loading**
   - Load raw CSV using Pandas
   - Inspect data with `head()`, `info()`, `describe()`

2. **Data Cleaning**
   - Convert date column to datetime
   - Handle missing values
   - Filter relevant columns
   - Export cleaned dataset

3. **Statistical Analysis**
   - Calculate daily, monthly, yearly mean, min, max, and standard deviation
   - Identify trends in temperature, rainfall, and humidity

4. **Visualizations**
   - Line chart: Daily temperature trends
   - Bar chart: Monthly rainfall totals
   - Scatter plot: Humidity vs temperature
   - Combined dashboard plot

5. **Grouping and Aggregation**
   - Group by month or season
   - Aggregate statistics for trends analysis

6. **Export and Reporting**
   - Save cleaned data as `cleaned_weather.csv`
   - Save plots in `/images/`
   - Summary insights saved in `summary.txt`

## Key Insights
- Temperature rises from winter to summer and falls towards winter
- Rainfall peaks during monsoon months (July–September)
- Humidity highest during rainy months, lowest in summer
- Inverse relationship between temperature and humidity observed
- Winter months have low rainfall and moderate temperatures

## How to Run

**Python script:**
```bash
python weather_analysis.py

Author
Arbaaz ali weather-data-visualizer-arbaazali

