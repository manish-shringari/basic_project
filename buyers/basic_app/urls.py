from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.CustomersListView.as_view(),name='customers_list'),
    #url(r'^appraisal/$',views.AppraisalView.as_view(),name='appraisal'),
    url(r'^appraisal/$',views.AppraisalView.as_view(),name='appraisal'),
    url(r'^inventory/$', views.InventoryView.as_view(), name='inventory'),
    url(r'^purchase/$', views.PurchaseView.as_view(), name='purchase'),
    url(r'^customers/(?P<pk>\d+)$', views.CustomersDetailView.as_view(), name='customers_detail'),
    url(r'^customers/new/$', views.CreateCustomersView.as_view(), name='customers_new'),
    ]