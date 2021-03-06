from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import Oder, Oders_Item


class OderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','created_at','updated_at')
    search_fields = ('customer_name',)

admin.site.register(Oder, OderAdmin)
admin.site.register(Oders_Item)