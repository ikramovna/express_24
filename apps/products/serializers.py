from rest_framework.serializers import ModelSerializer, Serializer

from apps.products.es_documents import ProductDocument
from apps.products.models import (Product, Category, Petition, Staff)
from apps.users.serializers import UserForSerializer


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # def save(self):
    #     product = super().save()
    #     product_document = ProductDocument(
    #         meta={'id': product.id},
    #         name=product.name,
    #         shot_description=product.short_description,
    #         long_description=product.long_description
    #     )
    #     product_document.save()
    #     return product


class ProductForDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'name', 'price'


class PetitionModelSerializer(ModelSerializer):
    user = UserForSerializer()
    product = ProductForDetailModelSerializer()

    class Meta:
        model = Petition
        fields = '__all__'


class StaffModelSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class SearchModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class SearchSerializer(Serializer):
    class Meta:
        document = ProductDocument
        fields = '__all__'


