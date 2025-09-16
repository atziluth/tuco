from django.db import models
from django.utils import timezone
from user.models import User, Customer

# Create your models here.
class Formula(models.Model):
    id = models.CharField(primary_key=True, max_length=10)          # 配方編碼
    name = models.CharField(max_length=50)                          # 配方名稱
    produce_date = models.DateField()                               # 配方生產日


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=15)          # 產品編碼
    name = models.CharField(max_length=30)                          # 產品名稱