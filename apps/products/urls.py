from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.products.views import (CategoryModelViewSet, ProductModelViewSet, ProductDetailRetrieveAPIView,
                                 PetitionModelViewSet, StaffModelViewSet, ProductSearchListAPIView,
                                 ElasticSearchViewSet)

routers = DefaultRouter()
routers.register('products', ProductModelViewSet)
routers.register('category', CategoryModelViewSet)
routers.register('petition', PetitionModelViewSet)
routers.register('staff', StaffModelViewSet)
routers.register('Elastic', ElasticSearchViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('product_detail/<int:pk>', ProductDetailRetrieveAPIView.as_view()),
    path('search', ProductSearchListAPIView.as_view()),
    # path('elasticsearch/', SearchProductAPIView.as_view()),

]
