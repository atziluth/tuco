from rest_framework import serializers

from .models import Formula, Product, Order


class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

