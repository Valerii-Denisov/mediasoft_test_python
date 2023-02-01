from rest_framework import viewsets

from .serializers import CitySerializer, StreetSerializer
from .models import City, Street


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ModelViewSet):
    serializer_class = StreetSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        city_id = self.kwargs['pk']
        city = City.objects.get(pk=city_id)
        filter_queryset = Street.objects.filter(city=city)
        print(City.objects.all())
        return filter_queryset
