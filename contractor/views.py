from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import ListView
from contractor.models import Tender
from .forms import TenderForm
from user.models import UserTender
from .models import Tender,ConfirmTender

# Create your views here.

def registertender(request):
    if request.method=="POST":
        form=TenderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Tender.objects.create(**form.cleaned_data)
            return redirect('/contractor/regsuccess/')
    else:
        form=TenderForm()
    context={'form':form}
    return render(request,"contractor/tenderform.html",context)

def regsuccess(request):
    return render(request,"contractor/regsuccess.html")

def contractorhome(request):
    return render(request,"contractor/contractor.html")

def tenderlist(request):
    uname=request.user.id
    query=Tender.objects.all().filter(ContractorName=uname)
    context={
        'data':query
    }
    return render(request,"contractor/tender_list.html",context)

def allbiddings(request):
    uname=request.user.username
    query=UserTender.objects.all().filter(Contractorname=uname)
    context={
        'data':query
    }
    return render(request,"contractor/allbiddings.html",context)

def confirmbiddings(request,tendername,username,bidprice):
    conname=request.user.username
    obj=ConfirmTender(Tendername=tendername,Contractorname=conname,Username=username,Bidprice=bidprice)
    obj.save()
    return render(request,"contractor/tender_confirm.html")

def profile(request):
    return render(request,"contractor/profile.html")