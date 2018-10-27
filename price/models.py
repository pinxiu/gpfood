from django.db import models

from ingredient.models import Ingredient
from store.models import Store


class History(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    price_num = models.DecimalField(max_digits=20, decimal_places=2)
    price_unit = models.CharField(max_length=200)
