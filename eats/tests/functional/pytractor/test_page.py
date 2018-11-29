import os
import unittest

from pytractor.exceptions import AngularNotFoundException
from pytractor.webdriver import WebDriverMixin

from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.element import Element
from eats.page import Page
from eats.common.exceptions import ElementNotFoundError, ElementClassError

__author__ = 'vtusan'

"""
Tests for page module using Firefox and Chrome drivers pytractor.
"""


class PytractorPageTestCase(PytractorTestBaseSetup):

    def setUp(self):
        super(PytractorPageTestCase, self).setUp()
        self.driver.get(self.base_url)

    def test_get_driver(self):
        class PageTest(Page):
            pass
        page = PageTest(self.driver, '/index.html')
        self.assertIsInstance(page.driver, WebDriverMixin)

    def test_get_name(self):
        class PageTest(Page):
            _name = "PageTest"
        page = PageTest(self.driver, '/index.html')
        self.assertEqual(page.name, "PageTest")

    def test_set_element_by_xpath(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, '/index.html')
        page.add_element('checkvalue', Element(page.driver, "//span[@id='checkValue']", 'xpath'))
        self.assertIsInstance(page.get_element('checkvalue'), Element)

    def test_get_element_by_load_element_init(self):
        class PageTest(Page):
            def _load_elements(self):
                self.add_element('checkvalue', Element(self.driver, "//span[@id='checkValue']", 'xpath'))

        page = PageTest(self.driver, '/index.html')
        self.assertIsInstance(page.get_element('checkvalue'), Element)

    def test_element_not_found_in_page_exception(self):
        class PageTest(Page):
            def _load_elements(self):
                self.add_element('checkvalue', Element(self.driver, "//span[@id='checkValue']", 'xpath'))

        page = PageTest(self.driver, '/index.html')
        with self.assertRaises(ElementNotFoundError):
            page.get_element('checkbox_not_exists')

    def test_get_element_default_xpath(self):
        class PageTest(Page):
            def _load_elements(self):
                self.add_element('checkvalue', Element(self.driver, "//span[@id='checkValue']"))

        page = PageTest(self.driver, '/index.html')
        self.assertEqual(page.get_element('checkvalue').search_by, 'xpath')

    def test_set_element_type_exception(self):
        class PageTest(Page):
            def _load_elements(self):
                self.add_element('checkbox', TestType(self.driver, "//div[@id='checkboxes']"))

        class TestType(object):
            def __init__(self, *args, **kwargs):
                pass

        with self.assertRaises(ElementClassError):
            PageTest(self.driver, '/index.html')

    def test_get_page_url(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, '/index.html')
        self.driver.get(self.base_url + '/index.html')
        self.assertEqual('/index.html', page.url)

    def test_get_page_source_with_js(self):
        class PageTest(Page):
            pass
        with open(os.path.join(self.process.get_application_path(), 'test_with_js_results.html'), 'r') as file:
            value = file.read()
        page = PageTest(self.driver, '/test_with_js.html')
        self.driver.ignore_synchronization = True
        self.driver.get(self.base_url + '/test_with_js.html')
        self.assertEqual(page.get_page_source(), value)

    def test_land_on_a_page_without_angular(self):
        with self.assertRaises(AngularNotFoundException):
            self.driver.get(self.base_url + '/test_no_angular.html')

    def test_get_meta_name_content(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, '/index.html')
        self.assertEqual(page.get_meta_name_content('description'), 'Angular Test Form Description')

    def test_get_favicon_info_not_in_html(self):
        class PageTest(Page):
            pass
        self.driver.ignore_synchronization = True
        self.driver.get(self.base_url + '/test_no_angular.html')
        page = PageTest(self.driver, '/test_no_angular.html')
        self.assertIsNone(page.get_favicon_info())

    def test_get_favicon_info_in_html(self):
        class PageTest(Page):
            pass
        self.driver.ignore_synchronization = True
        self.driver.get(self.base_url + '/test_with_favicon.html')
        page = PageTest(self.driver, '/test_with_favicon.html')
        self.assertEqual(page.get_favicon_info(), u'favicon.ico')

    def test_get_favicon_url(self):
        class PageTest(Page):
            pass
        self.driver.ignore_synchronization = True
        self.driver.get(self.base_url + '/test_no_angular.html')
        page = PageTest(self.driver, '/test_no_angular.html')
        self.assertEqual(page.get_favicon_url(), self.base_url + u'/favicon.ico')

    def test_go_to_page(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, '/index.html')
        self.assertFalse(page.goto())

    def test_i_am_on_page(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, '/index.html')
        self.assertFalse(page.i_am_on_page())

    def test_is_loaded(self):
        class PageTest(Page):
            pass
        page = PageTest(self.driver, '/index.html')
        self.assertFalse(page.is_loaded())

    @unittest.expectedFailure
    def test_add_element_only_accepts_elements(self):
        self.fail()
