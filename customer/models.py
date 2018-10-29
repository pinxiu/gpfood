from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer.username + "'s profile"
