from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet 
    # UserProfileView
)



router = routers.SimpleRouter()
router.register(r'', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),]





