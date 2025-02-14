# pylint: disable=W0401
# -*- coding: utf-8 -*-
from oscar_custom.oscar.core.loading import is_model_registered

from .abstract_models import AbstractLine, AbstractWishListSharedEmail, AbstractWishList

__all__ = []


if not is_model_registered("wishlists", "WishList"):

    class WishList(AbstractWishList):
        pass

    __all__.append("WishList")


if not is_model_registered("wishlists", "Line"):

    class Line(AbstractLine):
        pass

    __all__.append("Line")


if not is_model_registered("wishlists", "WishListSharedEmail"):

    class WishListSharedEmail(AbstractWishListSharedEmail):
        pass

    __all__.append("WishListSharedEmail")
