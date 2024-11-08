from project.common.models import BaseModel
from project.common.fields import CompressedImageField
from project.common.storages import MediaStorage

from django.utils.translation import gettext_lazy as _
from django.db import models


class LocationImage(BaseModel):
    image = CompressedImageField(
        storage=MediaStorage(),
        verbose_name=_("Фотография локаций"), null=True, blank=True,
        is_medium_thumbnail=True, upload_to="location_images/%Y/%m/%d"
    )
    location = models.ForeignKey(
        verbose_name=_("Локация"),
        to="Location",
        related_name="image_locations",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.location.name} - {self.id}"

    class Meta:
        db_table = "location_images"
        ordering = ["-created_at"]
        verbose_name = _("Фотография Локации")
        verbose_name_plural = _("Фотографии Локации")