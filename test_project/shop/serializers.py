from rest_framework import serializers

from .models import Shop
from test_project.city.serializers import CitySerializer, StreetSerializer
from test_project.city.models import City, Street


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'name',
            'city',
            'street',
            'house',
            'to_open_time',
            'to_close_time',
        )
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        #rep['city'] = CitySerializer(instance.city).data['name']
        #rep['street'] = StreetSerializer(instance.street).data['name']
        return rep