from project.common.models import BaseModel

from django.db import models
from django.utils.translation import gettext_lazy as _


class LocationFacility(BaseModel):
    android_icon = models.ImageField(
        verbose_name=_("Иконка Андроид"),
        upload_to='object_facility_icons/',
        null=True,
        blank=True
    )
    ios_icon = models.ImageField(
        verbose_name=_("Иконка IOS"),
        upload_to='object_facility_icons/',
        null=True,
        blank=True
    )
    web_icon = models.ImageField(
        verbose_name=_("Иконка Web"),
        upload_to='object_facility_icons/',
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name=_("Название удобства"),
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "location_facilities"
        ordering = ["-created_at"]
        verbose_name = _("Удобство Локации")
        verbose_name_plural = _("Удобства Локации")