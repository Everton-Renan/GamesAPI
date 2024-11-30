from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from Games_Reviews.utils import generate_api_key


def validate_review_value(value: int):
    if value > 5:
        raise ValidationError('The value cannot be greater than 5.')


class Review(models.Model):
    title = models.CharField(max_length=120)
    reviews = models.PositiveIntegerField(validators=[validate_review_value])
    image = models.ImageField(upload_to='images/%y/%m/')
    developer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    platforms = models.CharField(max_length=124)
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
                           blank=False,
                           max_length=50)

    def __str__(self) -> str:
        return self.user.username
