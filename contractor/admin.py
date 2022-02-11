from django.contrib import admin
from .models import Tender,Profile,ConfirmTender

# Register your models here.
admin.site.register(Tender)

admin.site.register(Profile)

admin.site.register(ConfirmTender)