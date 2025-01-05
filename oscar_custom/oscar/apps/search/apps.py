from django.urls import path
from django.utils.translation import gettext_lazy as _

from oscar_custom.oscar.core.application import OscarConfig
from oscar_custom.oscar.core.loading import get_class


class SearchConfig(OscarConfig):
    label = "search"
    name = "oscar_custom.oscar.apps.search"
    verbose_name = _("Search")

    namespace = "search"

    # pylint: disable=attribute-defined-outside-init
    def ready(self):
        self.search_view = get_class("search.views", "FacetedSearchView")

    def get_urls(self):
        urlpatterns = [path("", self.search_view.as_view(), name="search")]

        return self.post_process_urls(urlpatterns)
