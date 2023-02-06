from rest_framework import serializers

from .models import City, Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'name', 'city')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['city'] = CitySerializer(instance.city).data['name']
        return rep
