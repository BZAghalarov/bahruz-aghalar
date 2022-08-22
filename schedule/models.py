from django.db import models


# Create your models here.
class Agency(models.Model):
    agency_id = models.CharField(max_length=25)
    agency_name = models.CharField(max_length=125)
    agency_url = models.URLField()
    agency_timezone = models.CharField(max_length=25)
    agency_lang = models.CharField(max_length=25)
    agency_phone = models.CharField(max_length=30)
    agency_fare_url = models.URLField()