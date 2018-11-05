from django import forms

from .models import Customers, Vehicle


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = ('First_name','Last_name', 'Cell_number', 'Email', 'User_type')


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('vin',)