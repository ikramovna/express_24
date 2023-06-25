from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.products.models import (Product, Category, Petition, Staff)
from apps.products.serializers import (ProductModelSerializer, CategoryModelSerializer, PetitionModelSerializer,
                                       StaffModelSerializer)


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


# Petition API
class PetitionModelViewSet(ModelViewSet):
    queryset = Petition.objects.all()
    serializer_class = PetitionModelSerializer
    # permission_classes = (IsAdminOrReadOnly,)


# Staffs API
class StaffModelViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer

    # permission_classes = (IsAdminOrReadOnly,)

    @action(detail=False, methods=['get'])
    def count_accounts(self, request):
        count = self.get_queryset().count()
        return Response({'count': count})


class ProductSearchListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'short_description', 'long_description', 'price']
    permission_classes = [AllowAny]
