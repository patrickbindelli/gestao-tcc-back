import os
from django.db import models


class UsefulLink(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Título",
        help_text="Título do recurso a ser compartilhado",
    )
    url = models.URLField(
        blank=False,
        null=False,
        verbose_name="URL",
        help_text="URL do recurso a ser compartilhado",
    )

    class Meta:
        verbose_name = "Links Útil"
        verbose_name_plural = "Links Úteis"

    def __str__(self):
        return self.title


def file_upload_path(instance, filename):
    return os.path.join(f"useful_files", filename)


class UsefulFile(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Título",
        help_text="Título do recurso a ser compartilhado",
    )

    file = models.FileField(
        null=True,
        blank=True,
        upload_to=file_upload_path,
        verbose_name="Arquivo",
        help_text="Arquivo a ser compartilhado",
    )

    class Meta:
        verbose_name = "Arquivo Útil"
        verbose_name_plural = "Arquivos Úteis"

    def __str__(self):
        return self.title
