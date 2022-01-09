from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (
    OderViewSet 
    # UserProfileView
)



router = routers.SimpleRouter()
router.register(r'', OderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]





