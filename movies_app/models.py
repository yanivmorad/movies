from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=256, db_column="name", null=False)
    description = models.CharField(max_length=256, db_column="description", null=True)
    duration_min = models.FloatField(db_column="duration_min", null=False)
    release_year = models.IntegerField(db_column="release_year", null=True,
                                       validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    pic_url = models.URLField(max_length=512, db_column="pic_url", null=True)

    class Meta:
        db_table = 'movies'


class Rating(models.Model):
    class Meta:
        db_table = 'ratings'

    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT)
    rating = models.FloatField(db_column="rating", null=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
    rating_date = models.DateField(db_column="rating_date", null=True)


class Review(models.Model):
    class Meta:
        db_table = "reviews"
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT)
    review_text = models.CharField(max_length= 256,db_column="review_text",null=True)
    review_date = models.DateField(db_column="review_date",null=True)