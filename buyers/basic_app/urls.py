from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.CustomersListView.as_view(),name='customers_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^customers/(?P<pk>\d+)$', views.CustomersDetailView.as_view(), name='customers_detail'),
    url(r'^customers/new/$', views.CreateCustomersView.as_view(), name='customers_new'),
    ]