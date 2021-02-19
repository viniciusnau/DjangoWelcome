from datetime import datetime

from django.utils import timezone

from places.tasks import update_place_date


def test_should_insert_new_place(client):
    data = {'name': 'Normandy', 'description': 'A lot of peoples die in this place', 'date': datetime.now()}
    response = client.post('/places/', data=data)
    assert response.status_code == 201


def test_should_update_place_date(client, place):
    before_place_date = place.date

    update_place_date(place.id, datetime.now(tz=timezone.utc))
    place.refresh_from_db()

    assert before_place_date != place.date
