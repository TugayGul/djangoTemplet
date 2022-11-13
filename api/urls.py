from django.urls import path
import api.views


app_name = 'api'

urlpatterns = [
    path('product', api.views.ProductList.as_view(), name='product'),
    path('product/<int:product_id>', api.views.ProductDetail.as_view(), name='product_detail'),
    path('brand', api.views.BrandList.as_view(), name='brand'),
    path('product', api.views.OrderList.as_view(), name='order_list'),
    path('order/<int:order_id>', api.views.OrderDetail.as_view(), name='order_detail')
]
