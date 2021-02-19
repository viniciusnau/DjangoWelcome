import factory

from places.models import Place


class PlaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Place

    name = 'Normandy'
    description = 'A lot of people die in this place'
