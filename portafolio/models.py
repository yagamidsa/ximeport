from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField, datetime
# Create your models here.


class Skill(models.Model):
    imagenlugar = models.ImageField(upload_to="")
    carrera = CharField(max_length=100)
    lugarcarrera = CharField(max_length=250)
    descripcion = CharField(max_length=500)


class Project(models.Model):
    Empresa = CharField(max_length=100, null=True, verbose_name='Empresa')
    Cargo = CharField(max_length=100,null=True, verbose_name='Cargo')
    description = CharField(max_length=500,null=True, verbose_name='description')
    url = URLField(blank=True)
    Web = URLField(blank=True)
    date = models.DateTimeField(datetime.date.today)