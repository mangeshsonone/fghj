from django.db import models

# Create your models here.
class children(models.Model):
    Name=models.CharField(max_length=50)
    Branch=models.CharField(max_length=50)
    Division=models.CharField(max_length=50)