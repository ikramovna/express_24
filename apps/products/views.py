from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.products.models import (Product, Category, Petition, Staff)
from apps.products.permissions import IsAdminOrReadOnly
from apps.products.search_indexes import ProductIndex
from apps.products.serializers import (ProductModelSerializer, CategoryModelSerializer, PetitionModelSerializer,
                                       StaffModelSerializer, ElasticSearchSerializer)


# Product
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    # pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['post'])
    def count_total_price(self, request):
        product_ids = request.data.get('pk', [])
        total_price = 0

        for product_id in product_ids:
            try:
                product = Product.objects.get(id=product_id)
                total_price += product.price
            except Product.DoesNotExist:
                pass

        return Response({'total_price': total_price})


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

    # count total_price
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total_price = sum([product.price * product.quantity for product in queryset])
        return Response({"total_price": total_price})


# Staffs API
class StaffModelViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer

    # permission_classes = (IsAdminOrReadOnly,)

    @action(detail=False, methods=['get'])
    def count_accounts(self, request):
        count = self.get_queryset().count()
        return Response({'count': count})


# Product Search API
class ProductSearchListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'short_description', 'long_description']
    permission_classes = [AllowAny]


# connections.create_connection(alias='default', hosts=ELASTICSEARCH_DSL['default']['hosts'])


class ElasticSearchViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ElasticSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            search = ProductIndex.search().query('multi_match', query=query,
                                                 fields=['name', 'short_description', 'long_description'])
            ids = [hit.meta.id for hit in search]
            return Product.objects.filter(id__in=ids)
        return super(ElasticSearchViewSet, self).get_queryset()
