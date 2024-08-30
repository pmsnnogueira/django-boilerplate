"""
Core models module.
This module is used to store common models that are used in multiple apps.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractBaseModel(models.Model):
    """
    Abstract base model
    This model is used to store common fields in all models
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
        help_text=_("The date and time this record was created."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at"),
        help_text=_("The date and time this record was last updated."),
    )

    class Meta:
        abstract = True