from .models import Place
from project.celery import app


@app.task
def update_place_date(pk, date):
    Place.objects.filter(pk=pk).update(date=date)
