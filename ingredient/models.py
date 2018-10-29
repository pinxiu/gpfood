from django.db import models


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=200)
    quantity_num = models.IntegerField()
    quantity_unit = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredient_name


