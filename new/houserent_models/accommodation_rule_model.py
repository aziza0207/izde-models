from django.db import models
from django.utils.translation import gettext_lazy as _


class AccommodationRules(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Rules Title"))
    description = models.TextField(verbose_name=_("Rules Description"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self):
        return self.title