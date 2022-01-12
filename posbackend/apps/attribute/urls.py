from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (
    AtrributeViewSet,
    Attribute_ValueViewSet
)

router = routers.SimpleRouter()
router.register(r'', AtrributeViewSet, Attribute_ValueViewSet)


urlpatterns = [
    path('', include(router.urls))
]