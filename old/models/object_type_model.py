from project.common.models import BaseModel

from django.utils.translation import gettext_lazy as _
from django.db import models


class ObjectType(BaseModel):
    name = models.CharField(
        verbose_name=_("Название типа размещения"),
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    counter = models.IntegerField(
        verbose_name=_("Номер Типа Размещения"), default=0, null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "object_types"
        ordering = ["-created_at"]
        verbose_name = _("Тип Размещения Объекта")
        verbose_name_plural = _("Типы Размещения Объекта")