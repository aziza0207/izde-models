import calendar
from django.db import models
from django.utils.translation import gettext_lazy as _


class ObjectPrice(models.Model):
    start_month = models.IntegerField(
        choices=[(i, month) for i, month in enumerate(calendar.month_name) if month],
        verbose_name="Start Month"
    )
    start_day = models.IntegerField(choices=[(i, i) for i in range(1, 32)])
    end_month = models.IntegerField(
        choices=[(i, month) for i, month in enumerate(calendar.month_name) if month],
        verbose_name="End Month"
    )
    end_day = models.IntegerField(choices=[(i, i) for i in range(1, 32)])
    price = models.DecimalField(
        verbose_name=_("Цена"),
        max_digits=20, decimal_places=2,
        null=False, blank=False
    )
    accommodation = models.ForeignKey(
        verbose_name=_("Объект"),
        to="Accommodation",
        related_name="accommodation_prices",
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "accommodation_prices"
        ordering = ["-created_at"]
        verbose_name = _("Цена объекта")
        verbose_name_plural = _("Цены объекта")
