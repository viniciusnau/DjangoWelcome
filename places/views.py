import datetime

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from places.serializers import PlaceSerializer
from places.models import Place
from places.tasks import update_place_date


# Create your views here.


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by('date')
    serializer_class = PlaceSerializer

    @action(detail=True, methods=['get'])
    def update_date(self, request, pk):
        update_place_date.apply_async((pk, datetime.datetime.now(tz=timezone.utc)))
        return Response(status=HTTP_200_OK)
