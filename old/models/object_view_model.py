from project.common.models import BaseModel

from django.utils.translation import gettext_lazy as _
from django.db import models
from project.profiles.models import User


class LocationObjectView(models.Model):
    CLICK = 'click'
    VIEW = 'view'

    VIEW_TYPE_CHOICES = [
        (CLICK, _('Click')),
        (VIEW, _('View')),
    ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_("User"))
    location_object = models.ForeignKey(to="LocationObject", on_delete=models.CASCADE, verbose_name=_("Offer"),
                                        related_name="location_object_views")
    viewed_at = models.DateTimeField(auto_now_add=True, verbose_name=_("viewed_at"))
    type = models.CharField(max_length=10, choices=VIEW_TYPE_CHOICES, verbose_name=_("Type"))

    class Meta:
        db_table = "location_object_views"
        ordering = ["-viewed_at"]
        verbose_name = _('Просмотр Объекта')
        verbose_name_plural = _('Просмотры Объекта')
