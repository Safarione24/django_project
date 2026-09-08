from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(verbose_name="Имя", max_length=50)
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    patronimic = models.CharField(verbose_name="Отчество", max_length=50)


class Course(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.CharField(verbose_name='Описание')
    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(models.TextChoices):
        PEDING = 'pending', 'В ожидании'
        PROCCESSING = 'proccessing', 'В обработке'
        COMPLETED = 'completed', 'Выполнен'
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
