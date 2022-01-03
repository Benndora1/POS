from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import Oder


class OderAdmin(admin,ModelAdmin):
    list_display = ('customer_name')
    list_filter = ('is_admin','is_staff')

admin.site.register(Oder, OderAdmin)