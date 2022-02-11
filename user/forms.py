from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserTender
from contractor.models import Profile

class RawUserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserTenderForm(forms.ModelForm):
    class Meta:
        model=UserTender
        fields=[
            'Tendername',
            'Contractorname',
            'Name',
            'User',
            'Bidprice'
            ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']