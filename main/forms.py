from django.contrib.auth.forms import UserCreationForm
from main.models import CustomUser
from django import forms
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'patronimic', 'username', 'email', 'password', 'password1']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description'] 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['course', 'date']