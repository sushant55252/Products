



from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField(max_length = 250)
    weight = models.FloatField(max_length = 8)
    price = models.FloatField(max_length = 10)
    cost = models.FloatField(max_length = 10)
    category = models.TextField(max_length = 150)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

