from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qty = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    availabilty = models.CharField(max_length=100)
    # attribute_value_id
    # brand_id
    # categor_id
    # store_id
