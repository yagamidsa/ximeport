from django.shortcuts import render
from .models import Project
# Create your views here.
def exper(request):
    newvar = Project.objects.all()
    return render(request,'experiencia.html',{'projects': newvar})