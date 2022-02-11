from django.http import HttpRequest
from django.shortcuts import render,redirect
from .forms import RawUserForm
from contractor.models import Tender,ConfirmTender
from django.views.generic import ListView
from .forms import UserTenderForm,UserUpdateForm,ProfileUpdateForm
from .models import UserTender
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
class UserTenderlistview(ListView):
    model=Tender
    template_name="user/user_tender.html"
    context_object_name='tenders'

def signup(request):
    if request.method=="POST":
        form=RawUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('/login/')
    else:
        form=RawUserForm()
    return render(request,'user/registeruser.html',{'form':form})

def regusertender(request,tendername,contractorname,baseprice):
    print(baseprice)
    if request.method=="POST":
        form=UserTenderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            bidprice=request.POST.get('Bidprice')
            if int(bidprice) <= baseprice:
                return render(request,'login/invalid.html')
            UserTender.objects.create(**form.cleaned_data)
            return redirect('/contractor/regsuccess/')
    else:
        form=UserTenderForm(initial={'Tendername': tendername, 'Contractorname': contractorname, 'Bidprice': baseprice})
        
    context={'form':form}
    return render(request,"user/user_tender_reg.html",context)

def mybiddings(request):
    current_user=request.user
    uname=current_user.username
    print(uname)
    query=UserTender.objects.all().filter(Name=uname)
    # print(query.first())
    # for i in query:
    #     print(i.Name)
    # print(current_user)
    context={
        'data':query
    }
    return render(request,'user/userbiddings.html',context)

def userhome(request):
    return render(request,"user/userhome.html")

def confirmedbiddings(request):
    uname=request.user.username
    query=ConfirmTender.objects.all().filter(Username=uname)
    context={
        'data':query
    }
    return render(request,'user/userbiddings.html',context)

@login_required
def uprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user:uprofile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/uprofile.html', context)