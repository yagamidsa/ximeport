from django.shortcuts import render
from .models import Skill
from .models import Project


# Create your views here.
def home(request):
    newvar = Project.objects.all()
    var1 = Skill.objects.all()
    return render(request,'Home.html',{'projects': newvar,'experiencia':var1})
    


