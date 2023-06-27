from django.db.models import (CharField, CASCADE, Model, IntegerField, TextField, DateTimeField, ForeignKey, ImageField,
                              FloatField, TextChoices)
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=150)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=150)
    price = FloatField()
    short_description = TextField(blank=True, null=True)
    long_description = TextField(blank=True, null=True)
    quantity = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    category = ForeignKey('Category', CASCADE)
    owner = ForeignKey('auth.User', CASCADE)
    image = ImageField(upload_to='product/images/')

    def __str__(self):
        return self.name


class Petition(Model):
    user = ForeignKey('auth.User', CASCADE)
    product = ForeignKey(Product, CASCADE)
    quantity = IntegerField()
    phone = CharField(max_length=255)
    comment = TextField()

    class Status(TextChoices):
        DELIVERED = 'delivered', 'Delivered'
        NOT_DELIVERED = 'not delivered', 'Not Delivered'

    satus = CharField(max_length=15, choices=Status.choices, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Staff(Model):
    user = CharField(max_length=255)
    phone = CharField(max_length=50)

    class Role(TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        DELIVERER = 'deliverer', 'Deliverer'

    role = CharField(max_length=15, choices=Role.choices)
