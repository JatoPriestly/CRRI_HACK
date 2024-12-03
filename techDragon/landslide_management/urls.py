# landslide/urls.py
from django.urls import path
from .views import PredictLandslideArea

urlpatterns = [
    path('predict-area/', PredictLandslideArea.as_view(), name='predict_landslide_area'),
]
