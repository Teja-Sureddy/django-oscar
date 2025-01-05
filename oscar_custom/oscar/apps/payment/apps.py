from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig


class PaymentConfig(OscarConfig):
    label = "payment"
    name = "oscar_custom.oscar.apps.payment"
    verbose_name = _("Payment")
