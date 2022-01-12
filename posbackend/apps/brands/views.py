from django.db.models import fields
from django.shortcuts import render

from rest_framework import serializers, viewsets

# Create your views here.
from .models import Brands

class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('name', 'status')

class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
