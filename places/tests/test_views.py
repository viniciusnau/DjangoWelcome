from datetime import datetime


def test_should_insert_new_place(client):
    data = {'name': 'Normandy', 'description': 'A lot of peoples die in this place', 'date': datetime.now()}
    response = client.post('/places/', data=data)
    assert response.status_code == 201


def test_should_update_place_date(client, place):
    response = client.get(f'/places/{place.id}/update_date/')
    assert response.status_code == 200
