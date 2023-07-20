from rest_framework import serializers
from .models import Item, Category, Bid

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item # Which model to serailise
        fields = '__all__' # Which fields from object 
