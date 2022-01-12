from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import (
    BrandsViewSet
)

router = routers.SimpleRouter()
router.register(r'', BrandsViewSet)


urlpatterns = [
    path('', include(router.urls))
]