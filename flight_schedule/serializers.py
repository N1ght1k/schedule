from rest_framework import serializers
from .models import Departure, Arrival


class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = "__all__"


class ArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrival
        fields = "__all__"
