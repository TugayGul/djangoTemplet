from django.http import Http404
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from apples.product.models import Product, Brand
from apples.action.models import Order
from api.serializers import BrandSerializer, ProductSerializer, OrderSerializer
from api.filters.product import ProductFilter


class BrandList(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def post(self, request, *args, **kwargs):
        serializer = BrandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        brand = request.data.get('brand')
        name = request.data.get('name')
        description = request.data.get('description')
        weight = request.data.get('weight')
        daily_hiring_price = request.data.get('daily_hiring_price')

        try:
            brand = Brand.objects.get(name=brand)
        except:
            response = {
                'error': f'Brand with id {brand}, doesn\'t exist in DB.'
            }

            return Response(response, status.HTTP_400_BAD_REQUEST)

        product = Product(
            name=name,
            description=description,
            weight=weight,
            daily_hiring_price=daily_hiring_price,
            brand=brand
        )
        product.save()

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):

    @staticmethod
    def get_object(product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def post(self, request, product_id):
        product = self.get_object(product_id)

        name = request.data.get('name')
        description = request.data.get('description')
        weight = request.data.get('weight')
        daily_hiring_price = request.data.get('daily_hiring_price')
        brand_id = request.data.get('brand_id')
        brand_name = request.data.get('brand_name')
        if name:
            product.set_name(name)

        if description:
            product.set_description(description)

        if weight:
            product.set_weight(weight)

        if daily_hiring_price:
            product.set_daily_hiring_price(daily_hiring_price)

        if brand_id:
            product.set_brand_id(brand_id)

        if brand_name:
            product.set_brand_name(brand_name)

        product.save()

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, product_id):
        product = self.get_object(product_id)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        return Order.objects.filter(user=user)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')

        try:
            product = Product.objects.get(id=product_id)
        except:
            response = {
                'error': f'PRODUCT with id {product_id}, doesn\'t exist in DB.'
            }

            return Response(response, status.HTTP_400_BAD_REQUEST)

        try:
            start_at = datetime.strptime(request.data.get('start_at'), '%Y-%m-%d')
        except:
            response = {
                'error': 'Start date is not valid'
            }

            return Response(response, status.HTTP_400_BAD_REQUEST)

        try:
            end_at = datetime.strptime(request.data.get('end_at'), '%Y-%m-%d')
        except:
            response = {
                'error': 'End date is not valid'
            }

            return Response(response, status.HTTP_400_BAD_REQUEST)

        daily_hiring_price = product.get_daily_hiring_price()
        days_count = end_at - start_at
        total_price = days_count.days * daily_hiring_price

        order = Order(
            product=product,
            total_price=total_price,
            start_at=start_at.date(),
            end_at=end_at.date(),
            user=request.user
        )
        order.save()

        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetail(APIView):
    @staticmethod
    def get_object(order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, order_id):
        order = self.get_object(order_id)
        serializer = OrderSerializer(order)

        return Response(serializer.data)

    def delete(self, request, order_id):
        order = self.get_object(order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
