
from django.contrib import admin
from django.urls import path
from rest_framework_nested import routers



router = routers.SimpleRouter()
router.register(r'', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),]





