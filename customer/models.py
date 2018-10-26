from django.contrib.auth.models import User
from django.db import models

from recipe.models import Ingredient, Recipe

class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer.username + "'s profile"


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.customer.username + "'s cart"
