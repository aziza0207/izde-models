from project.common.models import BaseModel

from django.utils.translation import gettext_lazy as _
from django.db import models


class ObjectPatch(BaseModel):
    class Meta:
        db_table = "object_patch"
        ordering = ["-created_at"]
        verbose_name = _("Объект на редактировании")
        verbose_name_plural = _("Объекты на редактировании")

    edit_json = models.JSONField(
        verbose_name=_('Редактирование объекта')
    )
    location_object = models.ForeignKey(
        "LocationObject",
        on_delete=models.CASCADE,
        related_name='patch',
        verbose_name=_('Объект')
    )
    is_edited = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location_object}"