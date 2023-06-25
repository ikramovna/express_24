from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from apps.products.models import Product
from apps.users.models import (Order, Basket)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class UserForApplicationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone')




class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ('id',)


class BasketModelSerializer(ModelSerializer):
    class Meta:
        model = Basket
        exclude = ('id',)


class SearchModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()
