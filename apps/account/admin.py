from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "phone",
    )
    list_display_links = (
        "id",
        "phone",
    )
    search_fields = ("first_name", "last_name", "phone")
    filter_horizontal = ("groups", "user_permissions")

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )
    ordering = ("-date_joined",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )