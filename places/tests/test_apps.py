from django.apps import apps

from places.apps import PlacesConfig


def test_apps():
    assert PlacesConfig.name == 'places'
    assert apps.get_app_config('places').name == 'places'
