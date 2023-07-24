from django.contrib import admin
from .models import Category, Item
from .models import Photo
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Item)