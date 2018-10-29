from django.db import models

class Store(models.Model):
    store_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    visit = 1

    def __str__(self):
        return self.store_name
