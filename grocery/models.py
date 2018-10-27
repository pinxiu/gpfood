from django.db import models

from recipe.models import Ingredient


class Store(models.Model):
    store_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.store_name


class History(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    price_num = models.DecimalField(max_digits=20, decimal_places=2)
    price_unit = models.CharField(max_length=200)
