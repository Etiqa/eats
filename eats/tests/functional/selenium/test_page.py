import os
import unittest
import time
from selenium.webdriver import Firefox, Chrome
from testserver_selenium import SimpleWebServerProcessSelenium as SimpleServer
from eats.element import Element
from eats.page import Page
from eats.common.exceptions import ElementNotFoundInPage, ElementClassType

__author__ = 'vtusan'

"""
Tests for page module using Firefox and Chrome drivers selenium.
"""


class SeleniumPageTestBase(object):
    base_url = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.process = SimpleServer()
        cls.process.run()

    def setUp(self):
        self.base_url = "http://localhost:{}/".format(SimpleServer.PORT)
        self.driver = self.driver_class()
        self.driver.get(self.base_url + 'index.html#/form')
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.process.stop()

    def tearDown(self):
        self.driver.quit()

    def test_set_element_by_xpath(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, 'index.html#/form')
        page.set_element('checkbox', "//div[@id='checkboxes']", 'xpath')
        self.assertIsInstance(page.get_element('checkbox'), Element)

    def test_get_element_by_load_element_init(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']", 'xpath')

        page = PageTest(self.driver, 'index.html#/form')
        self.assertIsInstance(page.get_element('checkbox'), Element)

    def test_element_not_found_in_page_exception(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']", 'xpath')

        page = PageTest(self.driver, 'index.html#/form')
        with self.assertRaises(ElementNotFoundInPage):
            page.get_element('checkbox_not_exists')

    def test_get_element_default_xpath(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']")

        page = PageTest(self.driver, 'index.html#/form')
        self.assertTrue(page.get_element('checkbox').is_present())

    def test_set_element_type_exception(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']", element_class=TestType)

        class TestType(object):
            pass

        with self.assertRaises(ElementClassType):
            PageTest(self.driver, 'index.html#/form')

    def test_get_page_url(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, 'index.html#/form')
        self.assertEqual(page.current_url(), self.base_url + page.url)

    def test_get_page_source_with_js(self):
        class PageTest(Page):
            pass
        with open(os.path.join(os.path.dirname(__file__), 'testapp_selenium/test_with_js_results.html'), 'r') as file:
            value = file.read()
        page = PageTest(self.driver, 'test_with_js.html')
        self.driver.get(self.base_url + 'test_with_js.html')
        time.sleep(1)
        self.assertEqual(page.get_page_source(), value)

    def test_get_meta_name_content(self):
        class PageTest(Page):
            pass

        page = PageTest(self.driver, 'index.html#/form')
        self.assertEqual(page.get_meta_name_content('description'), 'Test Meta')

    def test_get_favicon_info_not_in_html(self):
        class PageTest(Page):
            pass
        self.driver.get(self.base_url + 'test_no_angular.html')
        time.sleep(1)
        page = PageTest(self.driver, 'test_no_angular.html')
        self.assertIsNone(page.get_favicon_info())

    def test_get_favicon_info_in_html(self):
        class PageTest(Page):
            pass
        self.driver.get(self.base_url + 'test_with_favicon.html')
        time.sleep(1)
        page = PageTest(self.driver, 'test_with_favicon.html')
        self.assertEqual(page.get_favicon_info(), u'favicon.ico')

    def test_get_favicon_url(self):
        class PageTest(Page):
            pass
        self.driver.get(self.base_url + 'test_no_angular.html')
        time.sleep(1)
        page = PageTest(self.driver, 'test_no_angular.html')
        self.assertEqual(page.get_favicon_url(), self.base_url + u'favicon.ico')

    def test_go_to_page(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']")

        page = PageTest(self.driver, 'index.html#/form')
        self.assertFalse(page.goto())

    def test_i_am_on_page(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']")

        page = PageTest(self.driver, 'index.html#/form')
        self.assertFalse(page.i_am_on_page())

    def test_is_loaded(self):
        class PageTest(Page):
            def _load_elements(self):
                self.set_element('checkbox', "//div[@id='checkboxes']")

        page = PageTest(self.driver, 'index.html#/form')
        self.assertFalse(page.is_loaded())


class FirefoxWebDriverTest(SeleniumPageTestBase, unittest.TestCase):
    driver_class = Firefox


class ChromeWebDriverTest(SeleniumPageTestBase, unittest.TestCase):
    driver_class = Chrome
