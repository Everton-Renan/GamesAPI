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


class GenerateKeys(models.Model):
    class Meta:
        verbose_name_plural = 'GenerateKeys'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(default=generate_api_key,
                           editable=False,
                           unique=True,
                           null=False,
                           blank=False)

    def __str__(self) -> str:
        return self.user.username
