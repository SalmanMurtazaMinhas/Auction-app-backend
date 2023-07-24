from django.db import models
from token_auth.models import User
from cloudinary.models import CloudinaryField
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Photo(models.Model):
  image = CloudinaryField('image')

class Bid(models.Model):
    bid_amount = models.IntegerField()
    bidder_id = models.IntegerField()
    item_id = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    # image_url = ArrayField( models.CharField(max_length=600))
    image_url = models.CharField(max_length=600)
    starting_bid = models.IntegerField()
    category =  models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    # current_bids = models.ForeignKey(Bid, related_name='bid', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"{self.name}"
    



class AuctionList(models.Model):
    item = models.CharField(max_length=255)
    bid = models.CharField(max_length=255)
