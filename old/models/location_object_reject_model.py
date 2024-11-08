from django.utils.translation import gettext_lazy as _
from django.db import models
from project.profiles.models import User


class LocationObjectReject(models.Model):
    VENDOR = 'vendor'
    CLIENT = 'client'

    REJECTED_BY_CHOICES = [
        (CLIENT, _('Client')),
        (VENDOR, _('View')),
    ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    location_object = models.ForeignKey(to="LocationObject", on_delete=models.CASCADE, verbose_name=_("Объект"),
                                        related_name="location_object_rejections")
    reject_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата отклонения"))
    rejected_by = models.CharField(max_length=10, choices=REJECTED_BY_CHOICES, verbose_name=_("Отклонено кем"))

    class Meta:
        db_table = "location_object_rejects"
        ordering = ["-reject_at"]
        verbose_name = _('Отказ по объекту')
        verbose_name_plural = _('Отказы по объектам')
