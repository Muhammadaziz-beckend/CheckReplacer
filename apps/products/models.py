from django.db import models
from utils.models import DataTimeAbstract

from django_resized import ResizedImageField


class Product(DataTimeAbstract):
    img = ResizedImageField(
        "Изображения",
        size=[1020, 950],
        upload_to="product/",
        blank=True,
        null=True,
        quality=90,
        force_format="WEBP",
    )
    name = models.CharField(
        "Названия",
        max_length=145,
    )
    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = 'Продукт' # Товар
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name