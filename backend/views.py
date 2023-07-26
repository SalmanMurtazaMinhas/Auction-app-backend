
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import ItemSerializer, BidSerializer, AuctionListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Item, Bid, AuctionList
from django.contrib import messages
from token_auth.models import User
from token_auth.serializer import UserSerializer
from django.core import serializers


from django.contrib.auth.decorators import login_required

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
        return Item.objects.filter()
    serializer_class = ItemSerializer


class PlaceBid(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request,  *args, **kwargs):
        # user's balance
        user_id = request.user.id

        current_user = User.objects.filter(id = user_id)
        print(current_user)
        current_money = current_user[0].money
        print(current_money)

        # print(request.data)

        data = request.data
        # print(data['newBid'])
        


        # Get the bid amount placed
        current_bid_placed = data['newBid']
        
        # Get the name of item being bid on
        current_item = data['item']
        # print(current_item['id'])
        # Get starting bid of item
        item_from_DB = Item.objects.filter(id = current_item['id'])
        # current_bids = item_from_DB[0].current_bids
        
        # print(current_bids)

        # Get starting bid amount
        starting_bid = item_from_DB[0].starting_bid


        min_bid = starting_bid

        # Check if there are any previous bids
                # previous_bids = AuctionList.objects.filter(item = current_item['id'])
                # print(previous_bids)
                # for bid in previous_bids:
                
                
        previous_bids = Bid.objects.filter(item_id = current_item['id'])

        for bid in previous_bids:
        # Check if any of these bids are higher than the minimum bid amount
            if int(bid.bid_amount) > int(min_bid):
                # If true, save min amount as the highest bid
                min_bid = bid.bid_amount

        # print(min_bid)
        

        # Check if new bid is higher than min amount
        if (int(current_money) - int(current_bid_placed) > 0):
            if int(current_bid_placed) > min_bid:
            # If true, save a bid with user name, bid amonut, and name of item
                data['bid_amount'] = int(current_bid_placed)
                data['bidder_id'] = int(user_id)
                data['item_id'] = int(current_item['id'])
                bidserializer = BidSerializer(data=data)
                # Checks whether the serializer has all of the data it needs
                print(bidserializer.is_valid())
                if bidserializer.is_valid():
                    # Saves that data to the Database
                    saved_bid = bidserializer.save()

                    # Save new balance
                    new_money = int(current_money) - int(current_bid_placed)
                    # current_user[0].money = new_money
                    print(current_user)
                    current_user.update(money= new_money)
                    

                    
                    return Response(bidserializer.data )
                else: 
                    print(bidserializer.errors)
                    return Response(None, status = 500)
            # If not, send error message
            else: 
                return Response("Bid amount is too low!", status = 200)

        else: 
            return Response("Not enough money ):", status = 200)


        



class ItemDetailsView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




class BidsList(APIView):

    def post(self, request):

        _item_id = request.data.get('item_id')
            # # pk = self.kwargs.get('pk',None)
            # last_bid = Bid.objects.filter(item_id = item_id).earliest('bid_amount')
            # print(last_bid)
        last_bid = Bid.objects.filter(item_id = _item_id).order_by('bid_amount').last()
            # last_bid = Bid.objects.filter(item_id = _item_id).latest('bid_amount')

        if last_bid:
                last_bid_amount = last_bid.bid_amount
                # print(last_bid_amount)
        else: 
                last_bid_amount = 0
            
            
        return Response(last_bid_amount, status = 200)
            

    # serializer_class = BidSerializer



    #     print('hi')
    # Get the bid amount placed
        # bid_amount = req
    # Get the name of item being bid on
    # Get all the bids related to this item
    # Get starting bid amount
    # Check if any of these bids are higher than the minimum bid amount
        # If true, save min amount as the highest bid
    
    # Check if new bid is higher than min amount
    # If true, save a bid with user name, bid amonut, and name of item
    # If not, send error message


# def get_item_details(req, item_id):
#     item = Item.objects.get(id=item_id)
#     return render(req, {'item': item})


class MyItemsListView(ListAPIView):
    def get_queryset(self):
        # print('hi')

        user = self.request.user
        return Item.objects.filter(owner=user)
    serializer_class = ItemSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FilterCategoryListView(ListAPIView):
    def post(self, request):
        print(self.request.data.get('cat'))
        primary_key = self.request.data.get('cat')
        # print(primary_key)
        items_of_cat =  Item.objects.filter(category=primary_key)
        print('hi')
        print(items_of_cat)
        cat_data = serializers.serialize('json', items_of_cat)
        print(cat_data)
        return Response(cat_data, status = 200)
    serializer_class = ItemSerializer


