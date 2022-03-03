from unicodedata import name
from django.urls import URLPattern, path,include
from .views import skill
from portafolio import views


app_name = 'portafolio'

urlpatterns = [

    path('', skill, name='skill'),
]