from django.conf.urls import url
from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarDashboardConfig

from oscar_rosetta.dashboard import views


class OscarRosettaDashboardConfig(OscarDashboardConfig):

    name = "oscar_rosetta.dashboard"
    label = "rosetta_dashboard"
    verbose_name = _('Translations')
    namespace = "rosetta_dashboard"

    default_permissions = ["is_staff"]

    index_view = views.IndexView

    def get_urls(self):
        urls = [
            url(r'^$', self.index_view.as_view(), name="rosetta-index-view"),
        ]
        return self.post_process_urls(urls)
