from rest_framework.serializers import ModelSerializer

from apps.products.models import (Product, Category)


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'