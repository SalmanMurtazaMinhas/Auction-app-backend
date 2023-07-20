from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Item
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