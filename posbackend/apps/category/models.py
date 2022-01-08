from django.db import models



STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    activate = models.CharField(max_length=100, choices=STATUS)
