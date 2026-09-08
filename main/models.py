from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    name = models.CharField(verbose_name="Имя", max_length=50)
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    patronimic = models.CharField(verbose_name="Отчество", max_length=50)

class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Описание", blank=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.CharField(verbose_name='Описание', max_length=255)  # Добавил max_length
    
    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'В ожидании'
        PROCESSING = 'processing', 'В обработке'  # Исправил опечатку
        COMPLETED = 'completed', 'Выполнен'
    
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    # Добавьте другие поля для заказа по необходимости
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)