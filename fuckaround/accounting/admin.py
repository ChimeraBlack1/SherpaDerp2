from django.contrib import admin
from .models import AccountTypes, Accounts

# Register your models here.
admin.site.register(AccountTypes)
admin.site.register(Accounts)

