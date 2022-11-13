from django_filters import rest_framework
from apples.product.models import Product


class ProductFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name="daily_hiring_price", lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name="daily_hiring_price", lookup_expr='lte')
    min_weight = rest_framework.NumberFilter(field_name="weight", lookup_expr='gte')
    max_weight = rest_framework.NumberFilter(field_name="weight", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ["daily_hiring_price", "weight"]