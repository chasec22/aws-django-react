from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
