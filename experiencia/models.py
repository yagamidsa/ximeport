from django.db import models
from django.db.models.fields import CharField, URLField
import datetime

# Create your models here.


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    url = URLField(blank=True)
    Web = URLField(blank=True)
    date = models.DateTimeField(datetime.date.today)
