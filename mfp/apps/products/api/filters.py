import django_filters
from django.db.models import Q
from django_filters.rest_framework import FilterSet
from apps.products.models import Product


class ProductFilter(FilterSet):

    def filter_min_price(self, qs, search, value):

        return qs.filter(price__gte=value)

    def filter_max_price(self, qs, search, value):
        value = float(value)
        value += value * 0.05
        return qs.filter(price__lte=value)

    def filter_name(self, qs, search, value):
        return qs.filter(name__icontains=value)

    name = django_filters.filters.CharFilter(method='filter_name')
    min_price = django_filters.filters.CharFilter(method='filter_min_price')
    max_price = django_filters.filters.CharFilter(method='filter_max_price')

    class Meta:
        model = Product
        fields = ['id']
