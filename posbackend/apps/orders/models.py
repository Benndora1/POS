from django.db import models
from django.db.models.deletion import  SET_NULL
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from apps.utils.models import Timestamps
# Create your models here.
User = get_user_model()

class Oder(Timestamps, models.Model):
    bill_no = models.CharField(max_length=255),
    customer_name = models.CharField(max_length=255, blank=True)
    customer_address = models.CharField(max_length=255, blank=True)
    customer_phone_number = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\1?\d{9,10}$')],blank=True)
    gross_amount = models.CharField(max_length=255)
    service_charge_rate = models.CharField(max_length=255)
    service_charge = models.CharField(max_length=255)
    vat_charge_rate = models.CharField(max_length=255)
    vat_charge = models.CharField(max_length=255)
    net_amount = models.CharField(max_length=255)
    discount = models.CharField(max_length=255)
    paid_status = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    

