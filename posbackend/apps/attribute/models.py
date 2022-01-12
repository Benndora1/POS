from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.translation import activate

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Attribute_Value(models.Model):
    Value = models.CharField(max_length=255)
    Attribute_id = models.ForeignKey(Attribute, on_delete=CASCADE)