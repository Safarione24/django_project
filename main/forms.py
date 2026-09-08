from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Category, Product, Order

class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    patronimic = forms.CharField(max_length=50, required=False)

    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'patronimic', 'username', 'email', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'status']