from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)