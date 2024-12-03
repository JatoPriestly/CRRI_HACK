import pandas as pd
import numpy as np
import random
from datetime import datetime

# Define the bounding box for Buea, Cameroon
min_lat = 4.1212
max_lat = 4.1761
min_lon = 9.2141
max_lon = 9.3002

# Generate synthetic data
def generate_rainfall_data(num_points=1000, start_date="2010-01-01", end_date=datetime.today().strftime('%Y-%m-%d')):
    # Generate random latitudes and longitudes within the bounding box
    latitudes = np.random.uniform(min_lat, max_lat, num_points)
    longitudes = np.random.uniform(min_lon, max_lon, num_points)

    # Generate random rainfall values (in mm)
    rainfall = np.random.uniform(0, 300, num_points)  # Random values between 0 and 300 mm

    # Generate random dates from 2010 to today
    dates = pd.date_range(start=start_date, end=end_date).to_pydatetime()
    random_dates = [random.choice(dates) for _ in range(num_points)]

    # Create the DataFrame
    df = pd.DataFrame({
        "Latitude": latitudes,
        "Longitude": longitudes,
        "Rainfall (mm)": rainfall,
        "Date": random_dates
    })
    
    return df

# Generate 1000 data points for the dataset
rainfall_data = generate_rainfall_data()

# Save the dataset to a CSV file
rainfall_data.to_csv("rainfall_data_2010_to_today.csv", index=False)

print("Dummy Rainfall Dataset Created from 2010 to Today!")
