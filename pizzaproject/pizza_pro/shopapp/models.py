from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')
    
