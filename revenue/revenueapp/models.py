"""Models module for the revenue app."""
from django.db import models

class Venue(models.Model):
    """A class for Venue data."""
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=50)
    # state = models.CharField(max_length=2)
    # zipcode = models.CharField(max_length=5)
    # phone = models.CharField(max_length=10)
    website = models.URLField(max_length=200)
    image = models.URLField(max_length=200)
