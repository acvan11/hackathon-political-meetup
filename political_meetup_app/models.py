from django.db import models

# Create your models here.


class Profile(models.Model):

    user_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, default='M')
    age = models.IntegerField()
    radius = models.IntegerField()
    gun_control = models.IntegerField()
    abortion = models.IntegerField()
    immigration = models.IntegerField()
    drugs = models.IntegerField()
    healthcare = models.IntegerField()
    latest = models.IntegerField()

    def __str__(self):
        return self.user_name


class Venue(models.Model):

    name = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
