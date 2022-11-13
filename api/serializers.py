from rest_framework import serializers
from apples.action.models import Order
from apples.product.models import Brand, Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        queryset=Brand.objects.all(),
        slug_field='name',
        required=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'weight', 'daily_hiring_price', 'brand']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'start_at', 'end_at', 'iha_id']
