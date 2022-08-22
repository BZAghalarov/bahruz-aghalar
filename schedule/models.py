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


class Calendar(models.Model):
    service_id = models.CharField(max_length=25)
    monday = models.CharField(max_length=25)
    tuesday = models.CharField(max_length=25)
    wednesday = models.CharField(max_length=25)
    thursday = models.CharField(max_length=25)
    friday = models.CharField(max_length=25)
    saturday = models.CharField(max_length=25)
    sunday = models.CharField(max_length=25)
    start_date = models.CharField(max_length=25)
    end_date = models.CharField(max_length=25)


class CalendarDates(models.Model):
    service_id = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
    exception_type = models.CharField(max_length=25)


class Routes(models.Model):
    route_id = models.CharField(max_length=25)
    route_short_name = models.CharField(max_length=45)
    route_long_name = models.CharField(max_length=125)
    route_desc = models.CharField(max_length=125, null=True)
    route_type = models.CharField(max_length=25)
    route_url = models.CharField(max_length=125, null=True)
    route_color = models.CharField(max_length=50, null=True)
    route_text_color = models.CharField(max_length=25, null=True)


class Shapes(models.Model):
    shape_id = models.CharField(max_length=35)
    shape_pt_lat = models.CharField(max_length=45)
    shape_pt_lon = models.CharField(max_length=45)
    shape_pt_sequence = models.IntegerField()


class Stops(models.Model):
    stop_id = models.CharField(max_length=20)
    stop_code = models.IntegerField()
    stop_name = models.CharField(max_length=125)
    stop_desc = models.CharField(max_length=100, null=True)
    stop_lat = models.CharField(max_length=100)
    stop_lon = models.CharField(max_length=100)
    zone_id = models.IntegerField(null=True)
    stop_url = models.URLField(null=True, blank=True)
    location_type = models.CharField(max_length=100, null=True)
    parent_station= models.CharField(max_length=100, null=True)
    wheelchair_boarding = models.CharField(max_length=100, null=True)


class StopTimes(models.Model):
    trip_id = models.CharField(max_length=75)
    arrival_time = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    stop_id = models.CharField(max_length=100)
    stop_sequence = models.IntegerField()
    pickup_type = models.CharField(max_length=100)
    drop_off_type = models.CharField(max_length=100)


class Trips(models.Model):
    route_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)
    trip_id = models.CharField(max_length=100)
    trip_headsign = models.CharField(max_length=100)
    direction_id = models.CharField(max_length=100)
    block_id = models.CharField(max_length=100)
    shape_id = models.CharField(max_length=100)