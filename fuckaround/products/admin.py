from django.contrib import admin
from .models import Products, MFP, Accessory

# Register your models here.
admin.site.register(Products)
admin.site.register(MFP)
admin.site.register(Accessory)