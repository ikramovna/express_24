from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.products.views import CategoryCreateAPIView, ProductModelViewSet, ProductDetailRetrieveAPIView

routers = DefaultRouter()
routers.register('products', ProductModelViewSet, 'products')
routers.register('category', CategoryCreateAPIView, 'category')
urlpatterns = [
    path('', include(routers.urls)),
    path('product_detail/<int:pk>', ProductDetailRetrieveAPIView.as_view(),),
]
