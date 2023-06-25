from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import (ListAPIView, get_object_or_404)
from rest_framework.permissions import (IsAuthenticated, AllowAny)
from rest_framework.response import (Response)
from rest_framework.views import (APIView)
from rest_framework.viewsets import (ModelViewSet)
from rest_framework_simplejwt.tokens import (RefreshToken)

from apps.products.models import (Product)
from apps.users.models import (Order, Basket)
from apps.users.serializers import (OrderModelSerializer, BasketModelSerializer, SearchModelSerializer)
from apps.users.services import (register_service, reset_password_service, reset_password_confirm_service)


# Register API
class RegisterAPIView(APIView):
    def post(self, request):
        response = register_service(request.data)
        if response['success']:
            return Response(status=201)
        return Response(response, status=405)


#  Reset Password API
class ResetPasswordAPIView(APIView):
    def post(self, request):
        responce = reset_password_service(request)
        if responce['success']:
            return Response({'message': 'sent'})
        return Response(responce, status=404)


# Reset Password Confirm API

class PasswordResetConfirmAPIView(APIView):

    def post(self, request, token, uuid):
        response = reset_password_confirm_service(request, token, uuid)
        if response['success']:
            return Response({'message': 'Password changed'})
        return Response(response, status=400)


# Logout API
class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = RefreshToken(request.user)
        token.blacklist()
        return Response(status=200)


# User Order API

class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

    # sum ordered product
    @action(detail=False, methods=['get'])
    def sum_ordered_product_prices(self, request):
        orders = self.get_queryset()
        total_price = 0

        for order in orders:
            for product in order.products.all():
                total_price += product.price * order.quantity

        return Response({'total_price': total_price})


# User Basket API
class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = self.queryset.filter(product_id=request.data.get('product'), user_id=request.data.get('user'))
        if data:
            que_data = data.get().quantity + request.data.get('quantity')
            data.update(quantity=que_data)
            return Response(status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(product_id=kwargs.get('pk'), user=request.user)
        instance = get_object_or_404(queryset)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# User Search API
