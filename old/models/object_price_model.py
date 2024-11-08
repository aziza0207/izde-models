from project.common.models import BaseModel

from django.utils.translation import gettext_lazy as _
from django.db import models


class ObjectPrice(BaseModel):
    start_month = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    start_day = models.IntegerField(choices=[(i, i) for i in range(1, 32)])
    end_month = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    end_day = models.IntegerField(choices=[(i, i) for i in range(1, 32)])
    price = models.DecimalField(
        verbose_name=_("Цена"),
        max_digits=20, decimal_places=2,
        null=False, blank=False
    )
    object = models.ForeignKey(
        verbose_name=_("Объект"),
        to="LocationObject",
        related_name="object_prices",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "object_prices"
        ordering = ["-created_at"]
        verbose_name = _("Цена объекта")
        verbose_name_plural = _("Цены объекта")

    def __str__(self):
        return f"{self.start_month, self.start_day}-{self.end_month, self.end_day}, {self.price}. {self.object}"
