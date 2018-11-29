# -*- coding: utf-8 -*-
import unittest
from eats.utils.sitemap import url_encode
from hamcrest import *


class TestSitemapUrlEncode(unittest.TestCase):

    def test_url_default_utf8_encode(self):
        url = url_encode(u"https://www.xyrem.com/es/información-de-prescripción-de-xyrem")
        assert_that(url, equal_to(u"https://www.xyrem.com/es/informaci%C3%B3n-de-prescripci%C3%B3n-de-xyrem"))

    def test_url_utf8_encode(self):
        url = url_encode(u"https://www.xyrem.com/es/información-de-prescripción-de-xyrem", 'utf8')
        assert_that(url, equal_to(u"https://www.xyrem.com/es/informaci%C3%B3n-de-prescripci%C3%B3n-de-xyrem"))


if __name__ == '__main__':
    unittest.main()