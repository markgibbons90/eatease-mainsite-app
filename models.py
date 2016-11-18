from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    """Restaurant model"""
    name = models.CharField(max_length=200)
    overall_rating = models.FloatField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    website = models.CharField(max_length=100)
    opening_times = models.ForeignKey('OpeningTimes', on_delete=models.CASCADE)

class Location(models.Model):
    """A restaurant's location"""
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)

class Coordinates(models.Model):
    """A restaurant's coordinates"""
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)

class OpeningTimes(models.Model):
    """A restaurant's opening times"""
    monday_open = models.IntegerField()
    monday_close = models.IntegerField()
    tuesday_open = models.IntegerField()
    tuesday_close = models.IntegerField()
    wednesday_open = models.IntegerField()
    wednesday_close = models.IntegerField()
    thursday_open = models.IntegerField()
    thursday_close = models.IntegerField()
    friday_open = models.IntegerField()
    friday_close = models.IntegerField()
    saturday_open = models.IntegerField()
    saturday_close = models.IntegerField()
    sunday_open = models.IntegerField()
    sunday_close = models.IntegerField()

class Review(models.Model):
    """Review model"""
    rating = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
