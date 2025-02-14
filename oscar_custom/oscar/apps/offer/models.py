# pylint: disable=W0401, W0614
from oscar_custom.oscar.apps.offer.abstract_models import (
    AbstractBenefit,
    AbstractCondition,
    AbstractConditionalOffer,
    AbstractRange,
    AbstractRangeProduct,
    AbstractRangeProductFileUpload,
)
from oscar_custom.oscar.apps.offer.results import (
    SHIPPING_DISCOUNT,
    ZERO_DISCOUNT,
    BasketDiscount,
    PostOrderAction,
    ShippingDiscount,
)
from oscar_custom.oscar.core.loading import is_model_registered

__all__ = [
    "BasketDiscount",
    "ShippingDiscount",
    "PostOrderAction",
    "SHIPPING_DISCOUNT",
    "ZERO_DISCOUNT",
]


if not is_model_registered("offer", "ConditionalOffer"):

    class ConditionalOffer(AbstractConditionalOffer):
        pass

    __all__.append("ConditionalOffer")


if not is_model_registered("offer", "Benefit"):

    class Benefit(AbstractBenefit):
        pass

    __all__.append("Benefit")


if not is_model_registered("offer", "Condition"):

    class Condition(AbstractCondition):
        pass

    __all__.append("Condition")


if not is_model_registered("offer", "Range"):

    class Range(AbstractRange):
        pass

    __all__.append("Range")


if not is_model_registered("offer", "RangeProduct"):

    class RangeProduct(AbstractRangeProduct):
        pass

    __all__.append("RangeProduct")


if not is_model_registered("offer", "RangeProductFileUpload"):

    class RangeProductFileUpload(AbstractRangeProductFileUpload):
        pass

    __all__.append("RangeProductFileUpload")

# Import the benefits and the conditions. Required after initializing the
# parent models to allow overriding them

from oscar_custom.oscar.apps.offer.benefits import *
from oscar_custom.oscar.apps.offer.conditions import *

from oscar_custom.oscar.apps.offer.benefits import __all__ as benefit_classes
from oscar_custom.oscar.apps.offer.conditions import __all__ as condition_classes

__all__.extend(benefit_classes)
__all__.extend(condition_classes)
