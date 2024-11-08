import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


class Accommodation(models.Model):
    """Помещение"""

    guest_house = models.ForeignKey(
        verbose_name=_("Гостевой Дом"),
        to="GuestHouse",
        related_name="accommodations",
        on_delete=models.CASCADE,
    )
    vendor = models.ForeignKey(
        verbose_name=_("Вендор"),
        to="Vendor",
        related_name="vendors",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("Название объекта"), max_length=255, null=False, blank=False
    )
    description = models.TextField(
        verbose_name=_("Описание объекта"), null=False, blank=False
    )
    room_quantity = models.PositiveSmallIntegerField(
        verbose_name=_("Количество комнат"), null=False, blank=False
    )
    occupancy = models.PositiveSmallIntegerField(
        verbose_name=_("Вместимость"), null=False, blank=False
    )
    facility = models.ManyToManyField(
        verbose_name=_("Удобства Помещения"),
        to="AccommodationFacility",
        related_name="accommodation_facilities",
    )
    accommodation_type = models.ForeignKey(
        verbose_name=_("Тип объекта размещения"),
        to="ObjectType",
        related_name="object_types",
        on_delete=models.CASCADE,
    )
    accommodation_kind = models.ForeignKey(
        verbose_name=_("Вид объекта"),
        to="ObjectKind",
        related_name="object_kinds",
        on_delete=models.CASCADE,
    )
    check_in = models.TimeField(
        verbose_name=_("Заезд"), default=datetime.time(14, 0), null=False, blank=False
    )
    check_out = models.TimeField(
        verbose_name=_("Выезд"), default=datetime.time(12, 0), null=False, blank=False
    )
    rules = models.TextField(
        verbose_name=_("Правило проживания в объекте"), null=False, blank=False
    )

    partnership = models.PositiveIntegerField(
        verbose_name=_("Комиссия партнера"),
        validators=[MaxValueValidator(100)],
        default=15,
    )

    currency = models.ForeignKey(
        verbose_name=_("Валюта"),
        to="profiles.Currency",
        related_name="object_currency",
        on_delete=models.SET_NULL,
        null=True,
    )
    cancellation_policy = models.ForeignKey(
        to="CancellationPolicy",
        on_delete=models.SET_NULL,
        related_name="cancellation_policy_accommodation",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "accommodation"
        ordering = ["-created_at"]
        verbose_name = _("Объект")
        verbose_name_plural = _("Объекты")
