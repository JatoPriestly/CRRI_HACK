import pandas as pd
import numpy as np
import random

# Define the bounding box for Buea (just an example)
min_lat = 4.1212
max_lat = 4.1761
min_lon = 9.2141
max_lon = 9.3002

# Generate synthetic data
def generate_landscape_data(num_points=1000):
    # Generate random latitudes and longitudes within the bounding box
    latitudes = np.random.uniform(min_lat, max_lat, num_points)
    longitudes = np.random.uniform(min_lon, max_lon, num_points)

    # Simulate elevation (in meters) between 200m to 1500m (example range for a mountainous area)
    elevation = np.random.uniform(200, 1500, num_points)

    # Simulate slope (degrees) based on elevation (higher elevation may have higher slope)
    slope = np.random.uniform(0, 45, num_points)

    # Simulate aspect (degrees, direction of the slope: 0-360 degrees)
    aspect = np.random.uniform(0, 360, num_points)

    # Simulate land cover types (random selection from a list of land cover categories)
    land_cover_types = ['forest', 'grassland', 'urban', 'water', 'wetland']
    land_cover = np.random.choice(land_cover_types, num_points)

    # Create the DataFrame
    df = pd.DataFrame({
        'Latitude': latitudes,
        'Longitude': longitudes,
        'Elevation (m)': elevation,
        'Slope (degrees)': slope,
        'Aspect (degrees)': aspect,
        'Land Cover': land_cover
    })
    
    return df

# Generate 1000 data points for the dataset
landscape_data = generate_landscape_data()

# Save the dataset to a CSV file
landscape_data.to_csv("dummy_landscape_data.csv", index=False)

print("Dummy Landscape Dataset Created!")
