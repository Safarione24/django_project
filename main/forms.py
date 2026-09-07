from django import forms
from .models import Category, Product  # ИСПРАВЛЕНО: объединены импорты

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']  # ИСПРАВЛЕНО: добавлено description

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']