from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.products.models import Product


@receiver(post_save, sender=Product)
def update_product_index(sender, instance, **kwargs):
    product_index = ProductIndex(meta={'id': instance.id})
    product_index.name = instance.name
    product_index.short_description = instance.short_description
    product_index.long_description = instance.long_description
    product_index.save()

@receiver(post_delete, sender=Product)
def delete_product_index(sender, instance, **kwargs):
    product_index = ProductIndex(meta={'id': instance.id})
    product_index.delete(ignore=404)
