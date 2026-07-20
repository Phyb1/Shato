"""
URL configuration for the Shato Sports Bar project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# --- Brand the Django admin so it matches the site (see templates/admin/base_site.html) ---
admin.site.site_header = "Shato Sports Bar Admin"
admin.site.site_title = "Shato Admin Portal"
admin.site.index_title = "Welcome to the Shato Sports Bar dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]

# Serve user-uploaded media (e.g. notice flyers) in development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
