from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Films(models.Model):
    title = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    genre = models.CharField(max_length=150)
    summary = models.TextField(default='', blank=True, null=True)
    image_url = models.CharField(max_length=3000, blank=True, default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    Type = models.CharField(max_length=200, default='')
    populor = models.BooleanField(default=False)


class Series(models.Model):
    title = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    genre = models.CharField(max_length=150)
    summary = models.TextField(default='', blank=True, null=True)
    image_url = models.CharField(max_length=3000, blank=True, default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    episode = models.PositiveIntegerField(null=True, blank=True)
    populor = models.BooleanField(default=False)


class English(models.Model):
    genre = models.CharField(max_length=300)
    image_url = models.CharField(max_length=3000, blank=True, default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class WatchlistItem(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user.username} - {self.film.title}'

class Kids(models.Model):
    title = models.CharField(max_length=300)
    language = models.CharField(max_length=300)
    genre = models.CharField(max_length=150)
    summary = models.TextField(default='', blank=True, null=True)
    image_url = models.CharField(max_length=3000, blank=True, default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

