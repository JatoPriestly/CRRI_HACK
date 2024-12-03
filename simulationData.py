import numpy as np
import pandas as pd

# Define the bounding box for the area of interest
min_lat, max_lat = 4.12, 4.15  # Latitude range
min_lon, max_lon = 9.20, 9.25  # Longitude range
resolution = 0.01  # Grid resolution in degrees (~111m)

# Generate grid points
latitudes = np.arange(min_lat, max_lat, resolution)
longitudes = np.arange(min_lon, max_lon, resolution)
grid_points = [(lat, lon) for lat in latitudes for lon in longitudes]

# Simulate features for each grid point
def simulate_features(lat, lon):
    # Simulated features
    elevation = np.random.uniform(100, 2000)  # Elevation in meters
    slope = np.random.uniform(0, 45)  # Slope in degrees
    rainfall = np.random.uniform(0, 500)  # Rainfall in mm
    soil_type = np.random.choice([0, 1, 2])  # Encoded soil type
    land_cover = np.random.choice([0, 1, 2, 3])  # Encoded land cover
    landslide_occurrence = np.random.choice([0, 1], p=[0.6, 0.4])  # 40% chance of landslide
    return [lat, lon, elevation, slope, rainfall, soil_type, land_cover, landslide_occurrence]

# Create the dataset
data = [simulate_features(lat, lon) for lat, lon in grid_points]

# Convert to a DataFrame
columns = ['Latitude', 'Longitude', 'Elevation (m)', 'Slope (degrees)', 
           'Rainfall (mm)', 'Soil Type', 'Land Cover', 'Landslide Occurrence']
df = pd.DataFrame(data, columns=columns)

# Save to CSV for reuse
df.to_csv('simulated_landslide_data.csv', index=False)
print("Simulated dataset created and saved as 'simulated_landslide_data.csv'.")
