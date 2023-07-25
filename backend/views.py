from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import ItemSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Item, Category
# Create your views here.


# Create an item to auction

class ItemCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    # Will run this when the view gets a post request 
    def post(self, request):
        user = request.user
        # print('User Is:', user)
        
        data = request.data
        data['owner'] = user.id
        # print(data)

        serializer = ItemSerializer(data=data)
    # Checks whether the serializer has all of the data it needs
        if serializer.is_valid():
            # Saves that data to the Database
            serializer.save()
            return Response(serializer.data)

        return Response(None, status = 500)


class ItemListView(ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(owner=user)
    serializer_class = ItemSerializer


class ItemDetailsView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# def get_item_details(req, item_id):
#     item = Item.objects.get(id=item_id)
#     return render(req, {'item': item})

def place_bid(req):
    # Get the bid amount placed
    bid_amount = req
    # Get the name of item being bid on
    # Get all the bids related to this item
    # Get starting bid amount
    # Check if any of these bids are higher than the minimum bid amount
        # If true, save min amount as the highest bid
    
    # Check if new bid is higher than min amount
    # If true, save a bid with user name, bid amonut, and name of item
    # If not, send error message

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer