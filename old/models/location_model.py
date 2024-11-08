from project.common.models import BaseModel

from django.utils.translation import gettext_lazy as _
from django.db import models


class Location(BaseModel):
    name = models.CharField(
        verbose_name=_("Название Локации"),
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    placement = models.ForeignKey(
        verbose_name=_("Расположение"),
        to="Placement",
        on_delete=models.CASCADE,
        related_name="location_placements",
    )
    street = models.CharField(
        verbose_name=_("Улица"), max_length=255, null=True, blank=True
    )
    house = models.CharField(
        verbose_name=_("Дом"), max_length=255, null=True, blank=True
    )
    address_link = models.URLField(
        verbose_name=_("Ссылка адреса"), null=False, blank=False
    )
    facility = models.ManyToManyField(
        verbose_name=_("Удобства"),
        to="LocationFacility",
        related_name="location_facilities",
    )
    rules = models.TextField(
        verbose_name=_("Правило проживания на территории"), null=False, blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "locations"
        ordering = ["-created_at"]
        verbose_name = _("Локация")
        verbose_name_plural = _("Локации")