from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Car
        # fields=['id','name', 'owner', 'description']
        fields='__all__'