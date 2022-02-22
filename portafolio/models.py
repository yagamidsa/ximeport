from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.


class Skill(models.Model):
    imagenlugar = models.ImageField(upload_to="portafolio\images")
    carrera = CharField(max_length=100)
    lugarcarrera = CharField(max_length=250)
    descripcion = CharField(max_length=250)
