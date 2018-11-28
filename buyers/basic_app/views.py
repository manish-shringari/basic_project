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
vin_num = None
class AppraisalView(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    redirect_field_name = 'basic_app/appraisal_detail.html'
    form_class = VehicleForm
    model = Vehicle
    # print self.cleaned_data

    # def post(self, request, *args, **kwargs):
    #     print 'here==========='
    #     print self.form_class
    #
    #     return super(AppraisalView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        # print 'Value is-----------------'
        # print(form.cleaned_data['vin'])
        # print (form.cleaned_data['vin_num'])
        global vin_num
        vin_num = (form.cleaned_data['vin_num'])
        print 'vin is =====', vin_num
        return super(AppraisalView, self).form_valid(form)


class AppraisalDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'appraisal_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AppraisalDetailView, self).get_context_data (**kwargs)
        data = barcode_decoder.get_data(vin_num)
        context['data'] = data
        return context


class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory.html'
    # def get_context_data(self, **kwargs):
    #     context = super(InventoryView, self).get_context_data(**kwargs)
    #     data = barcode_decoder.get_data(vin_num)
    #     context['data'] = data
    #     return context

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
