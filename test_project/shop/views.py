from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ShopSerializer
from .models import Shop
from test_project.city.models import Street


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer

    def get_queryset(self):
        if self.action == 'list':
            queryset = Shop.objects.all()
            street = self.request.query_params.get('street', default=None)
            city = self.request.query_params.get('city', default=None)
            is_open = self.request.query_params.get('open', default=None)
            if street is not None:
                queryset = queryset.filter(street=street)
            if city is not None:
                queryset = queryset.filter(city=city)
            if is_open == '0':
                queryset = [
                    element for element in queryset if element.is_open == 0
                ]
            elif is_open == '1':
                queryset = [
                    element for element in queryset if element.is_open == 1
                ]
            return queryset

    def create(self, request, *args, **kwargs):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            city_id = request.data.get('city')
            street_id = request.data.get('street')
            if street_id:
                street_city_id = getattr(
                    Street.objects.get(id=street_id),
                    'city_id',
                )
                if int(street_city_id) != int(city_id):
                    return Response(
                        "This street doesn't correspond to the specified city",
                        status.HTTP_400_BAD_REQUEST,
                    )
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                'Check the data. The field must be filled in.',
                status.HTTP_400_BAD_REQUEST,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
