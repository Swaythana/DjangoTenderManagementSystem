from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from matplotlib.style import context
from .forms import LoginForm
from user.models import UserTender

# Create your views here.
def main(request):
    return render(request,"login/main.html")

def login(request):
    form=LoginForm()
    context={'form':form}
    return render(request,"login/login.html",context)

def homepage(request):
    global uname
    uname=request.POST.get('username')
    pwd=request.POST.get('password')
    loginas=request.POST.get('LoginAs')
    user=authenticate(request,username=uname,password=pwd)
    print(uname,pwd,loginas)
    # user=User.objects.filter(username=uname).first()
    # print(user.password)
    instance=UserTender.objects.get(Name=uname)
    if(loginas=="Admin"):
        if uname=="Swaythana" and pwd=="*Goldfish24":
            return HttpResponseRedirect("/admin/")
    elif loginas=="Contractor":
        if user is not None:
            return render(request,"contractor/contractor.html")
    elif loginas=="User":
        if user is not None:
            global context
            context={
        'x':instance
        }
            return render(request,"user/userhome.html",context)
    return render(request,"login/invalid.html")

def hpage(request):
    print(request.user)
    return render(request,"login/loginas.html")