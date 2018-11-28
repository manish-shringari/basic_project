from django.contrib import admin

# Register your models here.
from .models import Customers, Vehicle


admin.site.register(Customers)
admin.site.register(Vehicle)