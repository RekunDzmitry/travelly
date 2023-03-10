from django.db import models

# Create your models here.

class Trip(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.place_name