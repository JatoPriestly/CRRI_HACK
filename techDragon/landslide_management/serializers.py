from rest_framework import serializers

class AreaPredictionSerializer(serializers.Serializer):
    min_lat = serializers.FloatField()  # Minimum latitude of the bounding box
    max_lat = serializers.FloatField()  # Maximum latitude of the bounding box
    min_lon = serializers.FloatField()  # Minimum longitude of the bounding box
    max_lon = serializers.FloatField()  # Maximum longitude of the bounding box
    resolution = serializers.FloatField(default=0.001)  # Grid resolution (default: ~111m)
