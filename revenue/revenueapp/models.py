"""Models module for revenueapp."""
from django.db import models
# Validation modules
from django.core.validators import MinLengthValidator

class Genre(models.Model):
    """A class for genres."""
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        """Return string representation of genre."""
        return self.name

class Venue(models.Model):
    """A class for Venue data."""
    name = models.CharField(
            "name of the venue",
            max_length=50,
            unique=True,
            validators=[MinLengthValidator(2, "Name must be greater than 1 character")]
    )
    address = models.CharField("street address", max_length=120)
    city = models.CharField("city", max_length=50)
    state = models.CharField("state", max_length=2)
    # zipcode = models.CharField(max_length=5)
    # phone = models.CharField(max_length=10)
    website = models.URLField("external venue website", max_length=200)
    image = models.URLField("link to an image of venue", max_length=200)
    genres = models.ManyToManyField(Genre, help_text="HINT: Select multiple genres with ctrl/cmd.")

    # override the __str__ method to return the name of the venue
    def __str__(self):
        return self.name


class Review(models.Model):
    """Model for a review of a venue."""
    # Venue that is being reviewed
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, unique=True, null=False)
    # overall_rating is an integer from 1 to 5 with a default of 1
    class StarRating(models.IntegerChoices):
        """Star rating for a venue."""
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4
        FIVE_STARS = 5
    seating_rating = models.IntegerField(
                        "seating",
                        choices=StarRating.choices,
                        default=StarRating.ONE_STAR
    )
    sound_rating = models.IntegerField(
                        "sound",
                        choices=StarRating.choices,
                        default=StarRating.ONE_STAR
    )
    scene_rating = models.IntegerField(
                        "scene",
                        choices=StarRating.choices,
                        default=StarRating.ONE_STAR
    )
    bathrooms_rating = models.IntegerField(
                        "bathrooms", 
                        choices=StarRating.choices,
                        default=StarRating.ONE_STAR
    )
    overall_rating = models.IntegerField(
                        "overall",
                        choices=StarRating.choices,
                        default=StarRating.ONE_STAR
    )
    comments = models.TextField("comments", max_length=500)