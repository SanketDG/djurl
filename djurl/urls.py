from django.conf.urls import patterns, include, url

urlpatterns = patterns('djurl.views',
                       url(r'^$', 'index', name='home'),
                       # for our home/index page

                       url(r'^(?P<short_id>\w{6})$',
                           'redirectOriginal', name='redirectOriginal'),
                       # when short URL is requested it redirects to original
                       # URL

                       url(r'^makeshort/$', 'shortenUrl', name='shortenUrl'),
                       # this will create a URL's short id and return the short
                       # URL
                       )
