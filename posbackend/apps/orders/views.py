from rest_framework import serializers, viewsets

from .models import Oder, Oders_Item

# Create your views here.


class OderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oder
        fields = ('customer_name', 'customer_address',
                  'gross_amount', 'service_charge_rate',
                  'service_charge', 'created_at',
                  'vat_charge_rate', 'updated_at',
                  'vat_charge', 'discount', 'net_amount',
                  'paid_status')
    # def create(self, validated_data):
    #     return Order.objects.create_user(**validated_data)


class OderViewSet(viewsets.ModelViewSet):
    queryset = Oder.objects.all()
    serializer_class = OderSerializer 


class Oder_ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Oders_Item
        fields = ('product_id', 'order_name', 'qty', 'rate', 'gross_amount')


class Oder_ItemViewSet(viewsets.ModelViewSet):
    queryset = Oders_Item.objects.all()
    serializer_class = Oder_ItemSerializer