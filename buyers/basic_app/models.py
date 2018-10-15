from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Customers(models.Model):
    user = models.ForeignKey('auth.User')
    product = models.CharField(max_length=200)
    purchased_date = models.DateTimeField(blank=True, null=True)

    def purchase(self):
        self.purchased_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("customers_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.user