from django.contrib import admin

from .models import Check, CheckProduct


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_display_links = (
        "id",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_filter = (
        "update_dt",
        "create_dt",
    )
    search_fields = (
        "id",
        "total_price",
    )


@admin.register(CheckProduct)
class CheckProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "check__pk",
        "product__pk",
        "price",
        "count",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_display_links = (
        "id",
        "check__pk",
        "product__pk",
        "price",
        "count",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_filter = (
        "check",
        "product",
    )
    search_fields = (
        "check__pk",
    )
