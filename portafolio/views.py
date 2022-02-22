from django.shortcuts import render
from .models import Skill

# Create your views here.
def home(request):
 return render(request,'Home.html')

def about(request):
    return render(request, 'about.html')


def skill(request):
    var1 = Skill.objects.all()
    return render(request, 'skill.html',{'experiencia':var1})

