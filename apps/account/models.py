from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
from django.contrib.auth.models import Group
from phonenumber_field.modelfields import PhoneNumberField

from utils.models import DataTimeAbstract


class User(DataTimeAbstract, AbstractUser):

    username = None
    email = None
    phone = PhoneNumberField(
        max_length=100,
        unique=True,
        verbose_name="номер телефона",
        blank=True,
        null=True,
    )
    groups = models.ManyToManyField(
        Group,
        related_name="account_users",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Уникальное имя обратной связи
    )

    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{str(self.phone) or self.first_name}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("-date_joined",)
