from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover/', blank=True, )

    datetime_create = models.DateTimeField(default=timezone.now, verbose_name=_('DateTimeCreate'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('DateTimeModified'))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])
    

class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product'), )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('Author'), )
    body = models.TextField(verbose_name=_('Body'), )
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('Stars'), )
    image = models.ImageField(verbose_name=_('Author Image'), upload_to='author/author_cover/', blank=True, )


    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('DateTimeCreate'), )
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('DateTimeModified'), )

    active = models.BooleanField(default=True, verbose_name=_('Active'), )

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()


    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    