from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import (
    AtrributeViewSet
)

router = routers.SimpleRouter()
router.register(r'', AtrributeViewSet)


urlpatterns = [
    path('', include(router.urls))
]