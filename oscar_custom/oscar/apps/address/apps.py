from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class AddressConfig(OscarConfig):
    label = "address"
    name = "oscar_custom.oscar.apps.address"
    verbose_name = _("Address")
