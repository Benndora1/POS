from django.db import models


# Create your models here.

# STATUS = (
#     ('active', 'Active'),
#     ('inactive', 'Inactive'),
# )


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_status = models.CharField(max_length=100)