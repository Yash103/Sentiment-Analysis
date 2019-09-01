from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Reg(models.Model):
    Username=models.CharField(max_length=30)
    Fullname=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)

class Review(models.Model):
    user=models.CharField(max_length=30)
    review=models.TextField()
    reviewtypes=models.CharField(max_length=30)
    date = models.DateTimeField(default=datetime.now)
