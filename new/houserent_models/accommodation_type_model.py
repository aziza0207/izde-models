from django.db import models
from django.utils.translation import gettext_lazy as _


class AccommodationType(models.Model):
    slug = models.SlugField("Слаг", blank=True)
    name = models.CharField(
        verbose_name=_("Название"),
        max_length=255,
        unique=True,
    )
    counter = models.IntegerField(
        verbose_name=_("Номер Типа Размещения"), default=0, null=True, blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "accommodation_types"
        ordering = ["-created_at"]
        verbose_name = _("Тип Размещения Объекта")
        verbose_name_plural = _("Типы Размещения Объекта")
