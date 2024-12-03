import pandas as pd
import numpy as np
import random

# Define the bounding box for Buea (for geographical coordinates)
min_lat = 4.1212
max_lat = 4.1761
min_lon = 9.2141
max_lon = 9.3002

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic correlated data
def generate_landslide_data(num_points=1000):
    # Generate random latitudes and longitudes within the bounding box
    latitudes = np.random.uniform(min_lat, max_lat, num_points)
    longitudes = np.random.uniform(min_lon, max_lon, num_points)

    # Generate Elevation (in meters) - correlated with slope
    elevation = np.random.uniform(100, 2000, num_points)  # Elevation range (100m to 2000m)

    # Generate Slope (in degrees) - higher slopes for higher elevation
    slope = np.random.normal(15, 10, num_points) + (elevation * 0.01)  # Slope is correlated with elevation
    slope = np.clip(slope, 0, 45)  # Ensure slope stays between 0 and 45 degrees

    # Generate Rainfall (in mm) - correlated with landslide risk
    rainfall = np.random.normal(150, 100, num_points) + (elevation * 0.1)  # Rainfall increases with elevation
    rainfall = np.clip(rainfall, 0, 500)  # Maximum rainfall capped at 500mm

    # Generate Soil Type (encoded as integers: 0=clay, 1=sand, 2=silt)
    soil_type = np.random.choice([0, 1, 2], num_points)  # 0 = clay, 1 = sand, 2 = silt

    # Generate Land Cover Type (forest, grassland, urban, etc.)
    land_cover = np.random.choice(['forest', 'grassland', 'urban', 'wetland'], num_points)

    # Generate Landslide Occurrence (0 = No landslide, 1 = Landslide)
    landslide_occurrence = np.random.binomial(1, 0.1, num_points)  # ~10% landslide occurrence

    # Create DataFrame
    df = pd.DataFrame({
        'Latitude': latitudes,
        'Longitude': longitudes,
        'Elevation (m)': elevation,
        'Slope (degrees)': slope,
        'Rainfall (mm)': rainfall,
        'Soil Type': soil_type,
        'Land Cover': land_cover,
        'Landslide Occurrence': landslide_occurrence
    })
    
    return df

# Generate 1000 data points
landslide_data = generate_landslide_data()

# Save to CSV
landslide_data.to_csv("dummy_landslide_data.csv", index=False)

print("Dummy Landslide Dataset Created!")
