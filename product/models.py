from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Product(BaseModel):
    name = models.CharField(
        _('name'), unique=True, error_messages={'unique': _('a product with that name exists')}, max_length=150
    )
    price = models.SmallIntegerField(_('price'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
