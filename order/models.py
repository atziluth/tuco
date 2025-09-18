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


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=15)                                  # 訂單編號
    # create_at = models.DateField(default=timezone.now)
    delivery_predict = models.DateField()                                                   # 預計交貨日
    delivery_actual = models.DateField()                                                    # 實際交貨日
    amount1 = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)    # 數量1
    unit1 = models.CharField(max_length=5, null=True, blank=True)                           # 單位1
    amount2 = models.CharField(max_length=10, null=True, blank=True)                        # 數量2
    unit2 = models.CharField(max_length=1, null=True, blank=True)                           # 單位2
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_creator')       # 製單人員
    reviewer1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_reviewer1')   # 審核者1
    reviewer2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_reviewer2')   # 審核者2
    note = models.CharField(max_length=200, null=True, blank=True)                          # 備註
    process = models.CharField(max_length=10)                                               # 流程規劃
    workstation = models.CharField(max_length=20)                                           # 流程監控

    create_at = models.DateTimeField(auto_now_add=True)                                     # 製單時間
    remove_at = models.DateTimeField(null=True, blank=True)                                 # 刪除時間

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)# 客戶編號
    customer_name = models.CharField(max_length=10)                                         # 客戶名稱
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)  # 產品編號
    product_name = models.CharField(max_length=30)                                          # 產品名稱
    formula = models.ForeignKey(Formula, on_delete=models.SET_NULL, null=True, blank=True)  # 配方編號