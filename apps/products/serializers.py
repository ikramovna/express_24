from rest_framework.serializers import ModelSerializer

from apps.products.models import (Product, Category, Petition, Staff)
from apps.users.serializers import UserForApplicationSerializer


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductForDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ('name', 'price',)


class PetitionModelSerializer(ModelSerializer):
    user = UserForApplicationSerializer()
    product = ProductForDetailModelSerializer()

    class Meta:
        model = Petition
        fields = '__all__'


class StaffModelSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
