from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    # service_charge_value
    # vat_charge_value
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    country = models.CharField(max_length=100)
    message = models.TextField()
    currency = models.CharField(max_length=100)
