from django.db.models import fields
from django.shortcuts import render

# Create your views here.
from .models import Attribute, Attribute_Value
from rest_framework import serializers, viewsets


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name', 'status')

class AtrributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer