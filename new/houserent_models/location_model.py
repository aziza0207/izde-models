from mptt import models as mptt_models
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(mptt_models.MPTTModel):
    slug = models.SlugField("Слаг", blank=True)
    name = models.CharField(_("Title"), max_length=50)
    parent = mptt_models.TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="placements",
    )
    depth = models.PositiveSmallIntegerField(
        verbose_name=_("Floor"),
        default=0,
    )

    synonyms = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

    class Meta:
        verbose_name = _("Расположение")
        verbose_name_plural = _("Расположения")
        app_label = "location"
