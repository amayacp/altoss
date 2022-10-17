from datetime import date
from django.db import models

# Create your models here.

class userdata(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    massage =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class register(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    date   = models.CharField(max_length=20)
    message =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class enquery(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    project = models.CharField(max_length=255)
    message =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

class apply(models.Model):
    course = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    place =  models.CharField(max_length=255)
    status = models.IntegerField(default=0)

