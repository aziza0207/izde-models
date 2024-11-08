from django.db import models
from django.utils.translation import gettext_lazy as _


class GuestHouseFacility(models.Model):
    """Удобства гостевого дома"""

    name = models.CharField("Название", max_length=50)
    slug = models.SlugField("Слаг", blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    class Meta:
        db_table = "guest_house_facilities"
        ordering = ["-created_at"]
        verbose_name = _("Удобство Гостевого Дома")
        verbose_name_plural = _("Удобства Гостевого Дома")

    def __str__(self):
        return self.name
