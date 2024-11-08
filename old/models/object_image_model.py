from project.common.models import BaseModel
from project.common.fields import CompressedImageField
from project.common.storages import MediaStorage

from django.utils.translation import gettext_lazy as _
from django.db import models


class ObjectImage(BaseModel):
    image = CompressedImageField(
        storage=MediaStorage(),
        verbose_name=_("Фотография Объекта"), null=True, blank=True,
        is_medium_thumbnail=True, upload_to="object_images/%Y/%m/%d"
    )
    object = models.ForeignKey(
        verbose_name=_("Объект"),
        to="LocationObject",
        related_name="image_objects",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.object} - {self.id}"

    class Meta:
        db_table = "object_images"
        ordering = ["-created_at"]
        verbose_name = _("Фотография Объекта")
        verbose_name_plural = _("Фотографии Объекта")