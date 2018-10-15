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

class AboutView(TemplateView):
    template_name = 'about.html'

class CustomersListView(ListView):
    model = Customers

    def get_queryset(self):
        return Customers.objects.filter(purchased_date__lte=timezone.now()).order_by('-purchased_date')

class CustomersDetailView(DetailView):
    model = Customers

class CreateCustomersView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'basic_appp/customers_detail.html'

    form_class = CustomersForm

    model = Customers

