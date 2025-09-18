from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.CharField(max_length=5)                     # 部門
    title = models.CharField(max_length=10)                         # 職稱
    identity = models.CharField(max_length=1)                       # 權限
    note = models.CharField(max_length=200, null=True, blank=True)  # 備註
    
    
class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=10)          # 客戶編號
    name = models.CharField(max_length=30)                          # 客戶名稱
    address = models.CharField(max_length=200)                      # 地址
    liaison = models.CharField(max_length=20)                       # 連絡窗口姓名
    phone = models.CharField(max_length=25)                         # 連絡窗口電話
    title = models.CharField(max_length=10)                         # 連絡窗口職稱
    delete_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name