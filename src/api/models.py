from django.utils.translation import gettext_lazy as _

from names_checking.models import BaseModel
from django.db import models


class NamesWoman(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = _('Имя женщины')
        verbose_name_plural = _('Имена женщин')


class NamesMan(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = _('Имя мужчины')
        verbose_name_plural = _('Имена мужчин')
