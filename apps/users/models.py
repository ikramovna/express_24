from django.db.models import (Model, ForeignKey, CASCADE, IntegerField)


class Order(Model):
    user = ForeignKey('User', CASCADE)
    # product = ForeignKey('Product', CASCADE)
    quantity = IntegerField(default=1)


class Basket(Model):
    # product = ForeignKey(Product, CASCADE, 'baskets')
    quantity = IntegerField(default=1)
    user = ForeignKey('auth.User', on_delete=CASCADE)

    # def __str__(self):
    #     return self.product
