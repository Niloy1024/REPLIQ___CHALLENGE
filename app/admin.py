from django.contrib import admin
from .models import Device,Transactions

admin.site.register(Transactions)
admin.site.register(Device)
