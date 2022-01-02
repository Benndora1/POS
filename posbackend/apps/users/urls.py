
from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers
from .views import (
    UserViewSet, 
    # UserProfileView
)



router = routers.SimpleRouter()
router.register(r'', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),]





