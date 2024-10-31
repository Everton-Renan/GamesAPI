from django.db import models


class Review(models.Model):
    title = models.CharField()
    reviews = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/%y/%m/')
    developer = models.CharField()
    publisher = models.CharField()
    series = models.CharField()
    platforms = models.CharField()
    release = models.DateField()

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    review = models.ForeignKey(
        Review, blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.genre


class Mode(models.Model):
    mode = models.CharField(max_length=50)
    review = models.ForeignKey(
        Review, blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.mode
