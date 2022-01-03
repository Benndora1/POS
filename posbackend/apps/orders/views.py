from rest_framework import serializers, viewsets

from .models import Oder



# Create your views here.
class OderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oder
        fields = ('customer_name', 'customer_address', 'gross_amount','service_charge_rate','service_charge','created_at','vat_charge_rate', 'updated_at','vat_charge','discount','net_amount','paid_status')
 
    # def create(self, validated_data):
    #     return Order.objects.create_user(**validated_data)

class OderViewSet(viewsets.ModelViewSet):
    queryset = Oder.objects.all()
    serializer_class = OderSerializer 