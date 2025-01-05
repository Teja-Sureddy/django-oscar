from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class OrderConfig(OscarConfig):
    label = "order"
    name = "oscar_custom.oscar.apps.order"
    verbose_name = _("Order")
