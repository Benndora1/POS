from django.db import models

# Create your models here.

class Oder(models.Model):
    bill_no = models.CharField(max_length=255),
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)