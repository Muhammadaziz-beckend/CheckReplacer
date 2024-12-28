from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Check, CheckProduct


@receiver(post_save, sender=CheckProduct)
def check_product_signal(sender, instance: CheckProduct, created, **kwargs):
    total = 0

    for i in instance.linked_check.check_products.all():
        total += i.total_price

    if instance.linked_check.total_price != total:

        instance.linked_check.total_price = total
        instance.linked_check.save()

    total_price = instance.product.price * instance.count

    if instance.total_price != total_price or instance.price != instance.product.price:
        instance.total_price = instance.product.price * instance.count
        instance.price = instance.product.price

        instance.save()
