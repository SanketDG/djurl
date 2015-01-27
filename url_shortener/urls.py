from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       # if the URL pattern match /admin/ then open up admin
                       # panel

                       url(r'', include(
                           'djurl.urls', namespace='djurl')),
                       # if anything rather then /admin/ then it will look for
                       # djurl/urls
                       )
