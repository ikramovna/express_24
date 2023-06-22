from django.db.models import (CharField, CASCADE, Model, IntegerField, TextField, DateTimeField, ForeignKey, ImageField)
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=150)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(Model):
    title = CharField(max_length=150)
    price = IntegerField()
    short_description = TextField(blank=True, null=True)
    long_description = TextField(blank=True, null=True)
    quantity = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey('Category', CASCADE)
    owner = ForeignKey('auth.User', CASCADE)
    image = ImageField(upload_to='product/images/')

    def __str__(self):
        return self.title
