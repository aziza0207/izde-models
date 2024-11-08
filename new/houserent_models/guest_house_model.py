from django.db import models
from django.utils.translation import gettext_lazy as _


class GuestHouse(models.Model):
    """Гостевой Дом"""

    name = models.CharField(
        verbose_name=_("Название гостевого дома"),
        max_length=255,
        unique=True,
    )

    facility = models.ManyToManyField(
        verbose_name=_("Удобства"),
        to="GuestHouseFacility",
        related_name="guest_house_facilities",
    )
    rules = models.TextField(
        verbose_name=_("Правило проживания на территории"), null=False, blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "guest_houses"
        ordering = ["-created_at"]
        verbose_name = _("Гостевой дом")
        verbose_name_plural = _("Гостевые дома")
