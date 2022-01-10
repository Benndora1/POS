from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from .views import (
    CategoryViewSet 
    # UserProfileView
)

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
# schema_view = get_schema_view(title='Category API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


router = routers.SimpleRouter()
router.register(r'', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]





