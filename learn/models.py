
# Create your models here.
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
