from django.contrib import admin

from apps.products.models import Product

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name',)


admin.site.register(Product)
