from django.db import models
from django.contrib.postgres.fields import ArrayField


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Album(models.Model):
    genre = models.ForeignKey(
        'Genre',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
        )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        null=True,
        blank=True
        )
    image = models.ImageField(
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name


class Track(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='tracks'
        )
    name = models.CharField(max_length=100)
    track_number = models.PositiveIntegerField()
    length = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        null=True,
        blank=True
        )
    artist = models.CharField(max_length=100)

    def __str__(self):
        return f'Album: {self.album}, Track: {self.name}'
