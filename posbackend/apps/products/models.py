from typing import Callable
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from apps.attribute.models import Attribute
from apps.brands.models import Brands
from apps.category.models import Category

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qty = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    availabilty = models.CharField(max_length=100)
    attribute_id = models.ForeignKey(Attribute, on_delete=CASCADE)
    brand_id = models.ForeignKey(Brands, on_delete=CASCADE)
    category_id = models.ForeignKey(Category, on_delete=CASCADE)

    # store_id
