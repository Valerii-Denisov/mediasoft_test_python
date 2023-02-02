from rest_framework import viewsets

from .serializers import ShopSerializer
from .models import Shop


class ShopViewSet(viewsets.ModelViewSet):
   # queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Shop.objects.all()

        street = self.request.query_params.get('street', default=None)
        city = self.request.query_params.get('city', default=None)
        open = self.request.query_params.get('open', default=None)
        for element in queryset:
            print(element)
            print(element.is_open)
        if street is not None:
            queryset = queryset.filter(street=street)
        if city is not None:
            queryset = queryset.filter(city=city)
        if open is not None:
            queryset = [element for element in queryset if element.is_open == open]
        return queryset
