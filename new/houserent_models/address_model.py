from django.db import models
from django.utils.translation import gettext_lazy as _


class Street(models.Model):
    slug = models.SlugField("Слаг", blank=True)
    name = models.CharField(verbose_name=_("Название"), max_length=255)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    class Meta:
        db_table = "streets"
        ordering = ["-created_at"]
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")


class Address(models.Model):
    location = models.ForeignKey(
        verbose_name=_("Расположение"),
        to="Location",
        on_delete=models.CASCADE,
        related_name="location_placements",
    )
    street = models.ForeignKey(
        verbose_name=_("Расположение"),
        to="Street",
        on_delete=models.CASCADE,
        related_name="address",
    )
    number = models.CharField(
        verbose_name=_("Дом"), max_length=255, null=True, blank=True
    )
    address_link = models.URLField(
        verbose_name=_("Ссылка адреса"), null=False, blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    class Meta:
        db_table = "addresses"
        ordering = ["-created_at"]
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")
