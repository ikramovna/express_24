from django.db.models import (CharField, CASCADE, Model, IntegerField, TextField, DateTimeField, ForeignKey, ImageField)
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=150)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Meal(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = CharField(max_length=255)
    image = ImageField(upload_to='meal/images/')
    category = ForeignKey('Category', CASCADE)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=150)
    price = IntegerField()
    short_description = TextField(blank=True, null=True)
    long_description = TextField(blank=True, null=True)
    quantity = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey('Category', CASCADE)
    owner = ForeignKey('auth.User', CASCADE)
    image = ImageField(upload_to='product/images/')

    def __str__(self):
        return self.name


# class Petition(Model):
#     name = ForeignKey('auth.User', CASCADE)
#     meal_name = ForeignKey('Meal', CASCADE)
#     price = ForeignKey('Meal', CASCADE)
#     quantity = IntegerField()
#     all_price = IntegerField()
#     phone = CharField(max_length=100)
#     comment = TextField()
