from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_image_url = models.CharField(max_length=600)
    email_address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=60)
    block_number = models.CharField(max_length=50)
    road_number = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    money = models.CharField(max_length=10, default='100')
