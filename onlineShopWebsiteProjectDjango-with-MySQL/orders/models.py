from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(default=False verbose_name=_('Is Paid'))

    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=700, verbose_name=_('Address'))

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('DateTimeCreate'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('DateTimeModified'))

    