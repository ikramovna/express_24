from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from apps.products.models import (Product, Category, Meal)
from apps.products.serializers import (ProductModelSerializer, CategoryModelSerializer, MealModelSerializer)


# Permission
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return request.user and request.user.is_staff


# Product
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]


# Product Detail
class ProductDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


# Category
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminOrReadOnly]


# Meal
class MealModelViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealModelSerializer
    permission_classes = [IsAdminOrReadOnly]
