from django.test import TestCase
from .models import Url
from .views import *


class UrlShortener(TestCase):
    def test_short_url_large(self):
        url = "http://www.example.com"
        Url(httpurl=url)
        short_url = get_short_code()
        self.assertLess(len(short_url), len(url))
