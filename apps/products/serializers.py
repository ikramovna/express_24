from rest_framework.serializers import ModelSerializer

from apps.products.models import (Product, Category, Petition)
from apps.users.serializers import UserSerializer


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PetitionModelSerializer(ModelSerializer):
    user = UserSerializer()
    product = ProductModelSerializer()

    class Meta:
        model = Petition
        fields = '__all__'


# class PetitionForDetailModelSerializer(ModelSerializer):
#
#     class Meta:
#         model = Petition
#         fields = '__all__'
