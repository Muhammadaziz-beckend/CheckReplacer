from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_img",
        "id",
        "name",
        "price",
        "update_dt",
        "create_dt",
    )
    list_display_links = (
        "id",
        "name",
        "price",
        "update_dt",
        "create_dt",
    )
    list_filter = (
        "update_dt",
        "create_dt",
    )
    search_fields = (
        "name",
        "id",
    )

    @admin.display(description="Изображение")
    def product_img(self, instance: Product):
        if instance.img:
            return mark_safe(f'<img src="{instance.img.url}" width="100px">')
        return "-"
