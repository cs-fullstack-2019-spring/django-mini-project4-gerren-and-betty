from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class CollectorModel(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    dateAccountCreated = models.DateField(default=timezone.now)
    userTableForeignKey = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username


class GameModel(models.Model):
    name = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    dateMade = models.DateField(default='')
    ageLimit = models.IntegerField(default=0)
    collector = models.ForeignKey(CollectorModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
