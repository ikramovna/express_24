from django.contrib.auth.models import AbstractUser
from django.db.models import (Model, ForeignKey, CASCADE, IntegerField, TextField)



class Order(Model):
    user = ForeignKey('auth.User', CASCADE)
    product = ForeignKey('products.Product', CASCADE)
    quantity = IntegerField(default=1)


class Basket(Model):
    product = ForeignKey('products.Product', CASCADE)
    quantity = IntegerField(default=1)
    user = ForeignKey('auth.User', CASCADE)
    comment = TextField()

    def __str__(self):
        return self.product
