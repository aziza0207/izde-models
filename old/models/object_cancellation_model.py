from project.common.models import BaseModel

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator


class ObjectCancellation(BaseModel):
    cancellation_hour = models.PositiveIntegerField(verbose_name=_("Часы возврата"))
    cancellation_percent = models.IntegerField(verbose_name=_("Процент возврата"),
                                               validators=[MaxValueValidator(100)])
    object = models.ForeignKey(
        verbose_name=_("Объект"),
        to="LocationObject",
        related_name="object_cancellations",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "object_cancellations"
        ordering = ["-created_at"]
        verbose_name = _("Возврат объекта")
        verbose_name_plural = _("Возврат объекта")