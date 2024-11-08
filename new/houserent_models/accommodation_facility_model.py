from django.db import models
from django.utils.translation import gettext_lazy as _


class AccommodationFacility(models.Model):
    slug = models.SlugField("Слаг", blank=True)
    android_icon = models.ImageField(
        verbose_name=_("Иконка Android"),
        upload_to="object_facility_icons/",
        null=True,
        blank=True,
    )
    ios_icon = models.ImageField(
        verbose_name=_("Иконка IOS"),
        upload_to="object_facility_icons/",
        null=True,
        blank=True,
    )
    web_icon = models.ImageField(
        verbose_name=_("Иконка Web"),
        upload_to="object_facility_icons/",
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_("Название удобства"),
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "accommodation_facilities"
        ordering = ["-created_at"]
        verbose_name = _("Удобство Размещения")
        verbose_name_plural = _("Удобства Размещения")
