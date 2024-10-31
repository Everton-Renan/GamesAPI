from django.contrib.auth.models import User
from django.db import models

from Games_Reviews.utils import generate_api_key


class Review(models.Model):
    title = models.CharField()
    reviews = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/%y/%m/')
    developer = models.CharField()
    publisher = models.CharField()
    series = models.CharField()
    platforms = models.CharField()
    release = models.DateField()
    genre = models.CharField(max_length=50)
    mode = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class NewUser(User):
    key = models.CharField(default=generate_api_key, editable=False)
