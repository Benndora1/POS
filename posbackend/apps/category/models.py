from django.db import models

from apps.orders.models import STATUS

# Create your models here.

# STATUS = (
#     ('active', 'Active'),
#     ('inactive', 'Inactive'),
# )


class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)