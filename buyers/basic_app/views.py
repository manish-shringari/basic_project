from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from basic_app.models import Customers
from django.utils import timezone
from basic_app.forms import CustomersForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AppraisalView(LoginRequiredMixin, TemplateView):
    template_name = 'appraisal.html'

class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory.html'

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
