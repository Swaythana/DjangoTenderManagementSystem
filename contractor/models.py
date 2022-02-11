from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Tender(models.Model):
    Tendername=models.CharField(max_length=120)
    # ContractorId=models.IntegerField()
    ContractorName=models.ForeignKey(User,on_delete=models.CASCADE)
    # ContractorName=models.CharField(max_length=120)
    Baseprice=models.IntegerField()
    Deadline=models.DateTimeField()

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

class ConfirmTender(models.Model):
    Tendername=models.CharField(max_length=120)
    Contractorname=models.CharField(max_length=120)
    Username=models.CharField(max_length=120)
    Bidprice=models.IntegerField()