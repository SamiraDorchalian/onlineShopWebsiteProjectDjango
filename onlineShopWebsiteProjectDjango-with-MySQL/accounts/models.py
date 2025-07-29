from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='author_user/author_cover/', blank=True, )

