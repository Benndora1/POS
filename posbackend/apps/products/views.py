from rest_framework import serializers, viewsets

from .models import Products
# Create your views here.

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'sku', 'qty','price')
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer