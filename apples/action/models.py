from django.db import models
from apples.product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    def __int__(self):
        return self.id

    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE, blank=False, null=False)
    total_price = models.IntegerField(blank=False, null=False)
    start_at = models.DateField(blank=False, null=False)
    end_at = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    @classmethod
    def get_all(cls):
        return cls.objects.all()
