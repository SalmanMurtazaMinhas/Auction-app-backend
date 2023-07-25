from django.urls import path
from .views import ItemCreateView, ItemListView, ItemDetailsView, place_bid, CategoryListView

# from .views import get_item_details



urlpatterns = [
    # path(url path, what to run)
    path('api/items/create/', ItemCreateView.as_view()),
    path('api/items/', ItemListView.as_view()),
    # path('/api/items/detail/${props.itemId}', get_item_details, name='get_item_details'),
    path('api/items/detail/<pk>', ItemDetailsView.as_view()),
    path('/api/items/bid', place_bid),
    path('api/category/list/', CategoryListView.as_view()),
]