from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class CommunicationConfig(OscarConfig):
    label = "communication"
    name = "oscar_custom.oscar.apps.communication"
    verbose_name = _("Communication")
