from django.contrib import admin
from django.urls import path, include, re_path

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

import os

urlpatterns = [
    path(f"{os.getenv('ADMIN_WORD')}/", admin.site.urls),
    path(f"{os.getenv('WAGTAIL_ADMIN_WORD')}/", include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    re_path(r'', include(wagtail_urls)),
]

