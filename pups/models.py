from django.db import models
from django.contrib.auth.models import User


class Puppy(models.Model):
    name = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    age = models.IntegerField()


class Profile(User):
    renter = models.BooleanField(default=True)
    puppy = models.ForeignKey(Puppy,
                              on_delete=models.CASCADE,
                              related_name='puppy')
