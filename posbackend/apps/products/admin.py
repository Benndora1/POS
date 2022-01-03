from re import search
from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','qty')
    search_fields = ('name',)

admin.site.register(Products, ProductsAdmin)