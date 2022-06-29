from rest_framework import serializers
from .models import Opendata


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opendata
        fields = '__all__'
