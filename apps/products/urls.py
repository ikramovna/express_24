from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.products.views import (CategoryModelViewSet, ProductModelViewSet, ProductDetailRetrieveAPIView,
                                 MealModelViewSet)

routers = DefaultRouter()
routers.register('products/', ProductModelViewSet)
routers.register('category/', CategoryModelViewSet)
routers.register('meal/', MealModelViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    path('product_detail/<int:pk>', ProductDetailRetrieveAPIView.as_view()),

]
