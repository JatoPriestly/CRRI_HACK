from celery import shared_task
from .views import PredictLandslideArea

@shared_task
def daily_area_scan():
    # Define area of interest
    min_lat, max_lat = 4.12, 4.15
    min_lon, max_lon = 9.20, 9.25
    resolution = 0.01

    # Simulate API call to PredictLandslideArea
    data = {
        "min_lat": min_lat,
        "max_lat": max_lat,
        "min_lon": min_lon,
        "max_lon": max_lon,
        "resolution": resolution
    }
    PredictLandslideArea().post(data)
