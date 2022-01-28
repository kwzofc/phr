from rest_framework import serializers
from phr.models import PHR


class PHRSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PHR