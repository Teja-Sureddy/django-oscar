from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class AnalyticsConfig(OscarConfig):
    label = "analytics"
    name = "oscar_custom.oscar.apps.analytics"
    verbose_name = _("Analytics")

    # pylint: disable=unused-import
    def ready(self):
        from . import receivers
