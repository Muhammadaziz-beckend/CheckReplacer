from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from utils.models import DataTimeAbstract


class Check(DataTimeAbstract):
    total_price = models.DecimalField(
        "Общая сумма",
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = "чек"
        verbose_name_plural = "чеки"

    def __str__(self):
        return f"{self.id}  сумма:{str(self.total_price)}"


class CheckProduct(DataTimeAbstract):
    check = models.ForeignKey(
        "Check",
        models.CASCADE,
        related_name="check_products",
    )
    product = models.ForeignKey(
        "products.Product",
        models.CASCADE,
        related_name="check_products",
        verbose_name="продукт",
    )
    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
    count = models.BigIntegerField(
        "количество",
        default=1,
    )
    total_price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )

    class Meta:
        verbose_name = "продукт чека"
        verbose_name_plural = "продуты чеков"

    def __str__(self):
        return f"{str(self.product_id.pk)} {str(self.total_price)}"
