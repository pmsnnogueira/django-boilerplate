"""
Core app configuration.
This module is used to store the configuration of the core app.
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    """
    Core app configuration class
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = _("Core")
    