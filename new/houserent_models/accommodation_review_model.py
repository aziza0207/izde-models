from django.db import models
from django.utils.translation import gettext_lazy as _
from .star_choice import STARS_CHOICE


class AccommodationReview(models.Model):
    user = models.ForeignKey(
        verbose_name=_("Автор отзыва"),
        to="User",
        on_delete=models.CASCADE,
        related_name="user_reviews",
    )
    accommodation = models.ForeignKey(
        verbose_name=_("Объект"),
        to="Accommodation",
        on_delete=models.CASCADE,
        related_name="object_reviews",
    )
    cost_effectiveness = models.IntegerField(
        verbose_name=_("Соотношение цены"), choices=STARS_CHOICE
    )
    facilities_rating = models.IntegerField(
        verbose_name=_("Удобства"), choices=STARS_CHOICE
    )
    purity = models.IntegerField(
        verbose_name=_("Чистота"), choices=STARS_CHOICE
    )
    location = models.IntegerField(
        verbose_name=_("Расположение"), choices=STARS_CHOICE
    )
    comment = models.TextField(verbose_name=_("Комментарий к отзыву"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return f"{self.user} - {self.accommodation}"

    class Meta:
        db_table = "accommodation_reviews"
        ordering = ["-created_at"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
