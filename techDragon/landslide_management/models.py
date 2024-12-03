from django.db import models

# Create your models here.

class Terrain(models.Model):
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    slope = models.FloatField()  # Slope of the terrain
    # include more needed fields

    def __str__(self):
        return f"Terrain data for {self.location}"
    

class LandslideHistory(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    magnitude = models.FloatField()
    impact = models.TextField()

    def __str__(self):
        return f"Landslide history for {self.location} on {self.date}"
    

