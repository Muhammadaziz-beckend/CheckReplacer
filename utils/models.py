from django.db import models


class DataTimeAbstract(models.Model):

    update_dt = models.DateTimeField(
        "дата обновления",
        auto_now=True,
    )
    create_dt = models.DateTimeField(
        "дата создания",
        auto_now_add=True,
    )

    class Meta:
        abstract = True