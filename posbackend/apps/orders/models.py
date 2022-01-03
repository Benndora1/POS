from django.db import models


from apps.utils.models import Timestamps
# Create your models here.

class Oder(Timestamps, models.Model):
    bill_no = models.CharField(max_length=255),
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    gross_amount = models.CharField(max_length=255)
    service_charge_rate = models.CharField(max_length=255)
    service_charge = models.CharField(max_length=255)
    vat_charge_rate = models.CharField(max_length=255)
    vat_charge = models.CharField(max_length=255)
    net_amount = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    paid_status = models.IntegerField()
    # user_id = models.ForeignKey
    

