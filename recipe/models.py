import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    quantity_num = models.IntegerField()
    quantity_unit = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredient_name


class Recipe(models.Model):
    dish_name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    instruction = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.dish_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
