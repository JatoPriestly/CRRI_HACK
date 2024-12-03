# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Terrain, LandslideHistory
# from .serializers import TerrainSerializer, LandslideHistorySerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['POST'])
# def predict_landslide(request):
#     # Here you would implement the logic for landslide prediction using the received data
#     # For now, let's return a placeholder response.
#     location = request.data.get("location")
#     slope = request.data.get("slope")
#     rainfall = request.data.get("rainfall")

#     # Placeholder: A real model would use the data here for prediction.
#     risk_level = "high" if slope > 30 and rainfall > 100 else "low"

#     return Response({"location": location, "predicted_risk": risk_level})

# # Create your views here.
# class TerrainViewSet(viewsets.ModelViewSet):
#     queryset = Terrain.objects.all()
#     serializer_class = TerrainSerializer


# class LandslideHistoryViewSet(viewsets.ModelViewSet):
#     queryset = LandslideHistory.objects.all()
#     serializer_class = LandslideHistorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model and scaler
model = joblib.load('/home/hack237/Desktop/CRRI_HACK/landslide_model.pkl')  # Pre-trained Random Forest model
scaler = StandardScaler()

# Simulated feature extraction function
# Replace this with actual data fetching logic for elevation, slope, rainfall, etc.
def extract_features(lat, lon):
    return {
        'elevation': np.random.uniform(100, 2000),  # Example elevation (m)
        'slope': np.random.uniform(0, 45),  # Example slope (degrees)
        'rainfall': np.random.uniform(0, 500),  # Example rainfall (mm)
        'soil_type': np.random.choice([0, 1, 2]),  # Example soil type (encoded as integers)
        'land_cover': np.random.choice([0, 1, 2, 3])  # Example land cover (encoded as integers)
    }

class PredictLandslideArea(APIView):
    def post(self, request):
        # Extract bounding box and resolution from request
        min_lat = request.data.get('min_lat')
        max_lat = request.data.get('max_lat')
        min_lon = request.data.get('min_lon')
        max_lon = request.data.get('max_lon')
        resolution = request.data.get('resolution', 0.001)  # Default resolution (degrees)

        # Validate input data
        if not (min_lat and max_lat and min_lon and max_lon):
            return Response({"error": "Bounding box coordinates are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate grid points within the bounding box
        latitudes = np.arange(min_lat, max_lat, resolution)
        longitudes = np.arange(min_lon, max_lon, resolution)
        grid_points = [(lat, lon) for lat in latitudes for lon in longitudes]

        # Extract features for each grid point
        extracted_data = [extract_features(lat, lon) for lat, lon in grid_points]
        df = pd.DataFrame(extracted_data)
        df[['Elevation (m)', 'Slope (degrees)', 'Rainfall (mm)']] = scaler.fit_transform(
            df[['elevation', 'slope', 'rainfall']]
        )
        df['Soil Type'] = df['soil_type']
        df['Land Cover'] = df['land_cover']

        # Predict landslide occurrence for all points
        X = df[['Elevation (m)', 'Slope (degrees)', 'Rainfall (mm)', 'Soil Type', 'Land Cover']]
        df['Landslide Occurrence'] = model.predict(X)

        # Calculate high-risk points
        high_risk_points = df[df['Landslide Occurrence'] == 1]
        high_risk_percentage = (len(high_risk_points) / len(df)) * 100

        # Trigger broadcast if high-risk percentage > 60%
        if high_risk_percentage > 60:
            send_broadcast_alert(high_risk_percentage)

        # Return response with risk analysis
        return Response({
            'total_points': len(df),
            'high_risk_points': len(high_risk_points),
            'high_risk_percentage': high_risk_percentage,
            'risk_status': "Broadcast Sent" if high_risk_percentage > 60 else "Normal"
        }, status=status.HTTP_200_OK)

def send_broadcast_alert(percentage):
    """
    Simulated function to send a broadcast alert.
    Replace this with actual notification logic (e.g., email, SMS, or webhook).
    """
    print(f"[ALERT] Landslide Risk: {percentage:.2f}% detected. Broadcast sent!")
