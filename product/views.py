from django.shortcuts import render
from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
