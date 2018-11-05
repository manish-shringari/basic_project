from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

USER_TYPE = (
    (1, "admin"),
    (2, "buyer"),
    (3, "manager"),
    (4, "Other"),
)


class Customers(models.Model):
    # user = models.ForeignKey('auth.User', null=True)
    First_name = models.CharField(max_length=200, null=True,blank=True)
    Last_name = models.CharField(max_length=200, null=True,blank=True)
    Cell_number = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    User_type = models.IntegerField('User Type', choices=USER_TYPE, null=True,blank=True)

    def get_absolute_url(self):
        return reverse("customers_detail",kwargs={'pk': self.pk})

    def __str__(self):
        return self.First_name

class Vehicle(models.Model):
    #document = models.FileField()
    vin = models.FileField(null=True,blank=True)
    make = models.CharField(max_length=200, null=True,blank=True)
    model = models.CharField(max_length=200, null=True,blank=True)

    def get_absolute_url(self):
        return reverse("inventory")

