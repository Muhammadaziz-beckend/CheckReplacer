from django.contrib import admin

from .models import Check, CheckProduct


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_display_links = (
        "id",
        "owner",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_filter = (
        "owner",
        "update_dt",
        "create_dt",
    )
    readonly_fields = ("total_price",)
    search_fields = (
        "id",
        "total_price",
    )


@admin.register(CheckProduct)
class CheckProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "linked_check__id",
        "product__id",
        "price",
        "count",
        "total_price",
        "update_dt",
        "create_dt",
    )
    list_display_links = (
        "id",
        "owner",
        "linked_check__id",
        "product__id",
        "price",
        "count",
        "total_price",
        "update_dt",
        "create_dt",
    )
    readonly_fields = (
        "price",
        "total_price",
    )
    list_filter = (
        "product",
        "linked_check",
        "owner",
    )
    search_fields = ("linked_check__id",)
