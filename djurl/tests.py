from django.test import TestCase
from .models import Url
from .views import *


class UrlShortener(TestCase):
    def test_short_url_large(self):
        url = "http://www.example.com"
        short_url = get_short_code()
        self.assertLess(len(short_url), len(url))

    def test_recover_original_url(self):
        url = "http://www.example.com"
        u = Url(httpurl=url)
        self.assertEqual(url, str(u))

    # def test_short_code_duplication(self):
    #     url = "http://www.example.com"
    #     u = Url(httpurl=url)
    #     sc = shorten_url(u.short_id)
    #     self.assertEqual(u.short_id, sc)

    # def test_short_id_redirection(self):
    #     url = "http://www.example.com"
    #     u = Url(httpurl=url)
    #     redirect_original(short_id=u.short_id)
    #     self.assertRedirects()
