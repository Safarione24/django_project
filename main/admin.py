from django.contrib import admin
from .models import Category, Product  # ИСПРАВЛЕНО: добавлены импорты

admin.site.register(Category)
admin.site.register(Product)