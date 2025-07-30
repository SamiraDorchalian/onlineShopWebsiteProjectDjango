from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid'))

    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    phone_number = models.CharField(max_length=15, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=700, verbose_name=_('Address'))

    order_notes = models.CharField(max_length=700, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('DateTimeCreate'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('DateTimeModified'))

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('Order'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name=_('Product'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))
    price = models.PositiveIntegerField(verbose_name=_('Price'))

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'
    