"""Models module for revenueapp."""
from django.db import models
# Validation modules
from django.core.validators import MinLengthValidator



class Venue(models.Model):
    """A class for Venue data."""
    name = models.CharField(
            "name of the venue",
            max_length=50,
            validators=[MinLengthValidator(2, "Name must be greater than 1 character")]
    )
    address = models.CharField("street address", max_length=120)
    city = models.CharField("city", max_length=50)
    state = models.CharField("state", max_length=2)
    # zipcode = models.CharField(max_length=5)
    # phone = models.CharField(max_length=10)
    website = models.URLField("external venue website", max_length=200)
    image = models.URLField("link to an image of venue", max_length=200)

    # override the __str__ method to return the name of the venue
    def __str__(self): 
        return self.name

class Review(models.Model):
    """Model for a review of a venue."""
    # Venue that is being reviewed
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=False)
    # overall_rating is an integer from 1 to 5 with a default of 1
    overall_rating = models.IntegerField("rate your overall experience", default=1)

