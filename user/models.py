from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserTender(models.Model):
    Tendername=models.CharField(max_length=120)
    Contractorname=models.CharField(max_length=120)
    Name=models.CharField(max_length=120)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Bidprice=models.IntegerField()

    def get_absolute_url(self):
        return reverse('user:userbiddings',args=[self.Name,])
    