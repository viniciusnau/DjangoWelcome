import datetime

from django.utils import timezone

from places.tasks import update_place_date


def test_should_update_place_date(client, place):
    before_place_date = place.date

    update_place_date(place.id, datetime.datetime.now(tz=timezone.utc))
    place.refresh_from_db()

    assert before_place_date != place.date
