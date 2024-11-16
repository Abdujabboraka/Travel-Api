from rest_framework import serializers, status
from .models import Travel, Klassi, Mehmonhona


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = "__all__"



class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klassi
        fields = "__all__"



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mehmonhona
        fields = "__all__"

