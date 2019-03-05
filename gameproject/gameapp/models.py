from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class CollectorModel(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=16)
    dateAccountCreated = models.DateField(timezone.now)
<<<<<<< HEAD
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


=======
    userTableForeignKey = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)


class GameModel(models.Model):
    name = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    dateMade = models.DateField(default='')
    ageLimit = models.IntegerField(default=0)
    collector = models.ForeignKey(CollectorModel, on_delete=models.CASCADE, null=True, blank=True)
>>>>>>> 26f7f2e3686a9dd22ae258d0d608451d8ba9c89c
