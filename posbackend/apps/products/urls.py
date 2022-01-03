from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import (
    ProductsViewSet
)

router = routers.SimpleRouter()
router.register(r'',ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]