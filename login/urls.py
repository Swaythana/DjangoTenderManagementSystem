from django.urls import path
from .views import main,login,homepage

urlpatterns = [
    path('',main),
    # path('login/',login),
    path('home/',homepage),
]