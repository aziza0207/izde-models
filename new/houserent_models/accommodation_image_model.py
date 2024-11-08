from django.db import models
from django.utils.translation import gettext_lazy as _


class AccommodationImage(models.Model):
    image = models.ImageField(

        verbose_name=_("Фотография Объекта")

    )
    object = models.ForeignKey(
        verbose_name=_("Объект"),
        to="LocationObject",
        related_name="image_objects",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "accommodation_images"
        ordering = ["-created_at"]
        verbose_name = _("Фотография Объекта")
        verbose_name_plural = _("Фотографии Объекта")
