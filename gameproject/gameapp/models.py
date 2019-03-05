from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Collector(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    dateAccountCreated = models.DateField(timezone.now)
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
