from rest_framework import serializers
from .models import Item, Category, Bid, AuctionList

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item # Which model to serailise
        fields = '__all__' # Which fields from object 

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid # Which model to serailise
        fields = '__all__' # Which fields from object 

class AuctionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionList # Which model to serailise
        fields = '__all__' # Which fields from object 
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PopulatedItemSerializer(ItemSerializer):
    category = CategorySerializer()
