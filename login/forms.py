from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

login=[('',''),
    ('Admin', 'Admin'),
    ('Contractor', 'Contractor'),
    ('User', 'User')]
    
class LoginForm(AuthenticationForm):
    LoginAs=forms.CharField(label='LoginAs', widget=forms.Select(choices=login))
    class Meta:
        model=User
        fields=['username','password','LoginAs']