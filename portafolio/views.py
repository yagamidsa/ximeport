from django.shortcuts import render
from .models import Skill
from .models import Project
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def home(request):
    if request.method=="POST":
        name = request.POST['name']
        message = request.POST['message'] + " - " + request.POST['email']
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["yagamidsa19@gmail.com"]
        send_mail(name + " Quiere Contactarte", message, email_from, recipient_list)
        
        
    newvar = Project.objects.all()
    var1 = Skill.objects.all()
    return render(request,'Home.html',{'projects': newvar,'experiencia':var1})
    


