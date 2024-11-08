from django.utils.translation import gettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid


class ObjectKind(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    android_icon = models.ImageField(
        verbose_name=_("Иконка Android"),
        upload_to='object_facility_icons/',
        null=True,
        blank=True
    )
    ios_icon = models.ImageField(
        verbose_name=_("Иконка IOS"),
        upload_to='object_facility_icons/',
        null=True,
        blank=True
    )
    web_icon = models.ImageField(
        verbose_name=_("Иконка Web"),
        upload_to='object_facility_icons/',
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name=_("Название вида"),
        max_length=255,
        null=False,
        blank=False,
        unique=True,
    )
    counter = models.IntegerField(
        verbose_name=_("Вместимость"), default=0, null=True, blank=True
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("Родительский вид")
    )

    is_deleted = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        db_table = "object_kinds"
        verbose_name = _("Вид Объекта")
        verbose_name_plural = _("Виды Объекта")
