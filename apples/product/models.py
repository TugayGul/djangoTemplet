from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.name}/'

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def set_name(self, name):
        self.name = name


class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=300, blank=True, null=False)
    weight = models.IntegerField(blank=False, null=False)
    daily_hiring_price = models.IntegerField(blank=False, null=False)
    brand = models.ForeignKey(Brand, related_name='prodcuts', on_delete=models.CASCADE, blank=False, null=False)

    def get_absolute_url(self):
        return f'/{self.name}/'

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_weight(self, weight):
        self.weight = weight

    def set_daily_hiring_price(self, daily_hiring_price):
        self.daily_hiring_price = daily_hiring_price

    def get_daily_hiring_price(self):
        return self.daily_hiring_price
