from django.db import models
from token_auth.models import User

# Create your models here.



class Bid(models.Model):
    bid_amount = models.IntegerField()
    # bidder = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    image = models.CharField(max_length=255)
    starting_bid = models.IntegerField()
    # category =  models.ForeignKey(Category, related_name='user', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"
    


    