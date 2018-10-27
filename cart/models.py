from django.contrib.auth.models import User
from django.db import models

from ingredient.models import Ingredient
from recipe.models import Recipe

class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.customer.username + "'s cart"
