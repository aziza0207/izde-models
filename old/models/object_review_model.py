from django.db import models

from project.houserent.constants import choices
from project.profiles.models.user import User
from project.houserent.models import LocationObject
from project.common.models import BaseModel
from django.utils.translation import gettext_lazy as _


class ObjectReview(BaseModel):
    user = models.ForeignKey(
        verbose_name=_("Автор отзыва"),
        to=User,
        on_delete=models.CASCADE,
        related_name="user_reviews",
    )
    object = models.ForeignKey(
        verbose_name=_("Объект"),
        to=LocationObject,
        on_delete=models.CASCADE,
        related_name="object_reviews",
    )
    quality = models.IntegerField(
        verbose_name=_("Соотношение цены"), choices=choices.STARS_CHOICE
    )
    conveniences = models.IntegerField(
        verbose_name=_("Удобства"), choices=choices.STARS_CHOICE
    )
    purity = models.IntegerField(
        verbose_name=_("Чистота"), choices=choices.STARS_CHOICE
    )
    location = models.IntegerField(
        verbose_name=_("Расположение"), choices=choices.STARS_CHOICE
    )
    comment = models.TextField(verbose_name=_("Комментарий к отзыву"))

    def __str__(self):
        return f"{self.user} - {self.object}"

    class Meta:
        db_table = "object_reviews"
        ordering = ["-created_at"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


