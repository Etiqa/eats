import unittest
import time

from selenium.webdriver import Remote, Firefox, Chrome
from testserver_selenium import SimpleWebServerProcessSelenium as SimpleServer
from eats.page import Page
from eats.application import Application
from eats.common import PageNameNone, PageNotFound

__author__ = 'vtusan'

"""
Tests for page module using Firefox and Chrome drivers pytractor.
"""


class SeleniumApplicationTestBase(object):
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

    def test_application_url(self):

        class TestApplication(Application):
            pass

        application = TestApplication(self.driver, self.base_url)
        self.assertEqual(application.base_url, self.base_url)

    def test_current_url(self):
        class TestApplication(Application):
            pass
        application = TestApplication(self.driver, self.base_url)
        self.driver.get(application.base_url)
        self.assertEqual(self.base_url + "#/form", application.current_url())

    def test_go_to_url_relative_path(self):
        class TestApplication(Application):
            pass
        application = TestApplication(self.driver, self.base_url)
        self.driver.get(application.base_url)
        application.go_to_url('/#/conflict')
        self.assertEqual(self.base_url + '/#/conflict', application.current_url())

    def test_go_to_url_full_path(self):
        class TestApplication(Application):
            pass
        application = TestApplication(self.driver, self.base_url)
        self.driver.get(application.base_url)
        application.go_to_url(self.base_url + '/#/conflict')
        self.assertEqual(self.base_url + '/#/conflict', application.current_url())

    def test_application_driver(self):

        class TestApplication(Application):
            pass

        application = TestApplication(self.driver, self.base_url)
        self.assertIsInstance(application.driver, Remote)

    def test_get_page_not_found_exception(self):

        class TestApplication(Application):
            pass

        application = TestApplication(self.driver, self.base_url)
        self.assertIsInstance(application.driver, Remote)
        with self.assertRaises(PageNotFound):
            application.get_page('NOT_EXISTS')

    def test_set_page_without_name_exception(self):
        class PageTest(Page):
            pass

        class TestApplication(Application):
            pass

            def _load_elements(self):
                self.add_page(PageTest(self.driver, self.base_url + "/#/form"))

        with self.assertRaises(PageNameNone):
            application = TestApplication(self.driver, self.base_url)

    def test_get_existing_page(self):
        class PageTest(Page):
                _name = "FORM"

        class TestApplication(Application):
            pass

            def _load_elements(self):
                self.add_page(PageTest(self.driver, self.base_url + "/#/form"))

        application = TestApplication(self.driver, self.base_url)
        self.assertIsInstance(application.get_page('FORM'), PageTest)

    def test_current_page(self):
        class PageTest(Page):
            _name = "FORM"

        class TestApplication(Application):
            pass

            def _load_elements(self):
                self.add_page(PageTest(self.driver, self.base_url + "/#/form"))

        application = TestApplication(self.driver, self.base_url)
        application.current_page = "FORM"
        self.assertEqual(application.current_page, application.get_page("FORM"))


class FirefoxWebDriverTest(SeleniumApplicationTestBase, unittest.TestCase):
    driver_class = Firefox


class ChromeWebDriverTest(SeleniumApplicationTestBase, unittest.TestCase):
    driver_class = Chrome
