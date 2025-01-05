from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class ShippingConfig(OscarConfig):
    label = "shipping"
    name = "oscar_custom.oscar.apps.shipping"
    verbose_name = _("Shipping")
