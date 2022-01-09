from django.db.models import fields, query
from django.shortcuts import render
from rest_framework import serializers, viewsets
# Create your views here.
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
     class Meta:
       model = Category
       fields = ('name', 'status')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer