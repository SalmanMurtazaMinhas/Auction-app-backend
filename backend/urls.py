from django.urls import path
from .views import ItemCreateView, ItemListView, ItemDetailsView, PlaceBid, BidsList, MyItemsListView, CategoryListView

# from .views import get_item_details



urlpatterns = [
    # path(url path, what to run)
    path('api/items/create/', ItemCreateView.as_view()),
    path('api/items/', ItemListView.as_view()),
    path('api/items/personal/', MyItemsListView.as_view()),
    # path('/api/items/detail/${props.itemId}', get_item_details, name='get_item_details'),
    path('api/items/detail/<pk>/', ItemDetailsView.as_view()),
    path('api/items/lastbid/', BidsList.as_view()),
    path('api/items/placebid/', PlaceBid.as_view()),
    # path('api/items/detail/<pk>/bid', place_bid, name="place_bid")

    path('api/category/list/', CategoryListView.as_view()),
]