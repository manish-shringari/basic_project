from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from basic_app.models import Customers, Vehicle
from django.utils import timezone
from basic_app.forms import CustomersForm, VehicleForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from basic_app import barcode_decoder

class AppraisalView(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    redirect_field_name = 'basic_app/inventory.html'
    form_class = VehicleForm
    model = Vehicle


class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory.html'
    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)
        data = barcode_decoder.get_data()
        context['data'] = data
        return context

class PurchaseView(LoginRequiredMixin, TemplateView):
    template_name = 'purchase.html'

class CustomersListView(LoginRequiredMixin, ListView):
    model = Customers

class CustomersDetailView(LoginRequiredMixin, DetailView):
    model = Customers

class CreateCustomersView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'basic_appp/customers_detail.html'
    form_class = CustomersForm
    model = Customers
