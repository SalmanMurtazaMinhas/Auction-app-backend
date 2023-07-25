from rest_framework import serializers
from .models import Item, Category, Bid

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item # Which model to serailise
        fields = '__all__' # Which fields from object 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PopulatedItemSerializer(ItemSerializer):
    category = CategorySerializer()
