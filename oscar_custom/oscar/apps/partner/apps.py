from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class PartnerConfig(OscarConfig):
    label = "partner"
    name = "oscar_custom.oscar.apps.partner"
    verbose_name = _("Partner")

    # pylint: disable=unused-import
    def ready(self):
        from . import receivers
