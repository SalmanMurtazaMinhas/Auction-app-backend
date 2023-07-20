from django.urls import path
from .views import ItemCreateView


urlpatterns = [
    # path(url path, what to run)
    path('api/items/create', ItemCreateView.as_view()),
    path('api/items/', ItemCreateView.as_view()),
]