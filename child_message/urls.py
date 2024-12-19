from django.conf import settings
from django.urls import include, path,re_path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images.views.serve import ServeView

from search import views as search_views

from home.views import *

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    re_path(
        r"^images/([^/]*)/(\d*)/([^/]*)/[^/]*$",
        ServeView.as_view(action="redirect"),
        name="wagtailimages_serve",
    ),
    path("", combined_view, name="home"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path("", include(wagtail_urls)),
    
     
]
