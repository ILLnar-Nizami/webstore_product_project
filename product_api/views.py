from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def product_page(request):
    return render(request, 'product_api/product_page.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'price']
    ordering_fields = ['name', 'price', 'quantity']

    @swagger_auto_schema(
        operation_description="List all products",
        responses={200: ProductSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        total_sum = sum(product.total_price for product in queryset)
        return Response({
            'products': serializer.data,
            'total_sum': total_sum
        })

    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={201: ProductSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a specific product by ID",
        responses={200: ProductSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a product (all fields required)",
        request_body=ProductSerializer,
        responses={200: ProductSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partial update of a product (only specified fields updated)",
        request_body=ProductSerializer(partial=True),
        responses={200: ProductSerializer()}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a product",
        responses={204: "No content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)