from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField()
    availabilty = models.IntegerField()
    # attribute_value_id
    # brand_id
    # categor_id
    # store_id
