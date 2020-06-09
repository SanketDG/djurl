from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="home"),
    # for our home/index page
    url(r"^(?P<short_id>\w{6})$", views.redirect_original, name="redirect_original"),
    # when short URL is requested it redirects to original
    # URL
    url(r"^makeshort/$", views.shorten_url, name="shorten_url"),
    # this will create a URL's short id and return the short
    # URL
]
