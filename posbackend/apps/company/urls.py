
from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers, urlpatterns
from .views import (
    CompanyViewSet
)


router = routers.SimpleRouter()
router.register(r'', CompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]