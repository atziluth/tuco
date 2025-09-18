from django.shortcuts import render
from django.utils.timezone import make_aware
from rest_framework import response, permissions, views, viewsets, generics, mixins, status

import datetime

from order import models, serializers

# Create your views here.

class FormulaViewSet(viewsets.ModelViewSet):
    queryset = models.Formula.objects.all()
    serializer_class = serializers.FormulaSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer