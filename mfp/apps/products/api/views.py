from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from apps.products.models import Product
from apps.products.api.serializers import ProductListSerializer
from apps.products.api.filters import ProductFilter


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination
    filter_class = ProductFilter

    def get(self, *args, **kwargs):
        print('here1')
        return super().get(*args, **kwargs)

