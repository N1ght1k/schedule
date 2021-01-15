from django.db import models


class Departure(models.Model):
    aircompany = models.CharField(max_length=45)
    flight_number = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    terminal = models.IntegerField()
    gate = models.IntegerField()
    flight_time = models.DateTimeField()
    flight_id = models.CharField(max_length=45)
    aircraft = models.CharField(max_length=45)
    reg_start = models.DateTimeField(null=True)
    reg_end = models.DateTimeField(null=True)
    boarding_start = models.DateTimeField(null=True)
    boarding_end = models.DateTimeField(null=True)
    desk = models.CharField(max_length=45, null=True)


class Arrival(models.Model):
    aircompany = models.CharField(max_length=45)
    flight_number = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    terminal = models.IntegerField()
    flight_time = models.DateTimeField()
    flight_id = models.CharField(max_length=45)
    aircraft = models.CharField(max_length=45)
