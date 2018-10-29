import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from ingredient.models import Ingredient


class Recipe(models.Model):
    dish_name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    instruction = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    img = 'https://lh3.googleusercontent.com/proxy/wore-t-h5VEQ0DOxy3yvWO2p7fDAO0NO5BhiBh1Wrg7z-dzZ0iFHwpfBXhv3-4WNtXYOtWCEp7z-chHyfCo0fX7JJ-R65nPg_DbvhLTvMiP8fSEuiPDkelJa92fF__2KEOu_uCXKlE6gvZeUsPOGWFHA6zVoBcTrrShqxCsbtlVRLcOyJF5Ewe_VMwkIxeNzLXwDhFIP=w1152'
    dish_type = 'Main Dish'
    time = '10 min'

    def __str__(self):
        return self.dish_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
