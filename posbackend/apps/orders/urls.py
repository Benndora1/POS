from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (
    Oder_ItemViewSet,
    OderViewSet 
    # UserProfileView
)



router = routers.SimpleRouter()
router.register(r'', OderViewSet)
router.register(r'', Oder_ItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]





