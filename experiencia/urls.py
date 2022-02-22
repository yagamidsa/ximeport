from django.urls import URLPattern, path
from .views import exper



app_name = 'experiencia'

urlpatterns = [

    path('experiencia/',exper,name='experiencia')

]