from django.db import models
from django.contrib.auth.models import User

from pups import stripe_settings


class Puppy(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='puppy')
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    age = models.IntegerField()
    rented_now = models.BooleanField(default=False)


class UserProfile(models.Model):
    active_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    renter = models.BooleanField(default=False)
    address = models.CharField(max_length=100, default=None)



