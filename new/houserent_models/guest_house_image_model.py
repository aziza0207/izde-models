from django.db import models
from django.utils.translation import gettext_lazy as _


class GuestHouseImage(models.Model):
    image = models.ImageField()
    guesthouse = models.ForeignKey(
        verbose_name=_("Гостевой Дом"),
        to="Accommodation",
        related_name="image_locations",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    class Meta:
        db_table = "guesthouse_images"
        ordering = ["-created_at"]
        verbose_name = _("Фотографии Гостевого Дома")
        verbose_name_plural = _("Фотографии Гостевых Домов")
