from unicodedata import name
from django.urls import URLPattern, path,include
from .views import about,skill
from portafolio import views


app_name = 'portafolio'

urlpatterns = [

    path('about/', about, name='about'),
    path('skill/', skill, name='skill'),
]