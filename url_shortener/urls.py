from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    # if the URL pattern match /admin/ then open up admin
    # panel
    url(r"", include(("djurl.urls", "djurl"), namespace="djurl")),
    # if anything rather then /admin/ then it will look for
    # djurl/urls
]
