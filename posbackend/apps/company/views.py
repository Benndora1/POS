from django.db.models import query
from rest_framework import serializers, viewsets

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name', 'address','phone','country','message','currency')

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer