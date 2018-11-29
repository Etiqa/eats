import unittest

from pytractor.webdriver import WebDriverMixin

from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.page import Page
from eats.element import Element
from eats.application import Application
from eats.common import PageNameIsNoneError, PageNotFoundError, ElementNotFoundError

__author__ = 'vtusan'

"""
Tests for page module using Firefox and Chrome drivers pytractor.
"""


class PytractorApplicationTestCase(PytractorTestBaseSetup):

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
        self.assertEqual(self.base_url + '/', application.current_url())

    def test_go_to_url_relative_path(self):
        class TestApplication(Application):
            pass
        application = TestApplication(self.driver, self.base_url)
        self.driver.get(application.base_url)
        application.go_to_url('/page.html')
        self.assertEqual(self.base_url + '/page.html', application.current_url())

    def test_go_to_url_full_path(self):
        class TestApplication(Application):
            pass
        application = TestApplication(self.driver, self.base_url)
        self.driver.get(application.base_url)
        application.go_to_url(self.base_url + '/index.html')
        self.assertEqual(self.base_url + '/index.html', application.current_url())

    def test_application_driver(self):

        class TestApplication(Application):
            pass

        application = TestApplication(self.driver, self.base_url)
        self.assertIsInstance(application.driver, WebDriverMixin)

    def test_get_page_not_found_exception(self):

        class TestApplication(Application):
            pass

        application = TestApplication(self.driver, self.base_url)
        self.assertIsInstance(application.driver, WebDriverMixin)
        with self.assertRaises(PageNotFoundError):
            application.get_page('NOT_EXISTS')

    def test_set_page_without_name_exception(self):
        class PageTest(Page):
            pass

        class TestApplication(Application):
            pass

            def _load_elements(self):
                self.add_page(PageTest(self.driver, self.base_url + "/index.html"))

        with self.assertRaises(PageNameIsNoneError):
            TestApplication(self.driver, self.base_url)

    def test_get_existing_page(self):
        class PageTest(Page):
                _name = "PAGE"

        class TestApplication(Application):
            pass

            def _load_elements(self):
                self.add_page(PageTest(self.driver, self.base_url + "/page.html"))

        application = TestApplication(self.driver, self.base_url)
        self.assertIsInstance(application.get_page('PAGE'), PageTest)

    def test_current_page(self):
        class PageTest(Page):
            _name = "PAGE"

        class TestApplication(Application):
            pass

            def _load_elements(self):
                self.add_page(PageTest(self.driver, self.base_url + "/page.html"))

        application = TestApplication(self.driver, self.base_url)
        page = application.get_page('PAGE')
        application.current_page = page
        self.assertEqual(application.current_page, application.get_page("PAGE"))

    @unittest.expectedFailure
    def test_add_element_only_accepts_pages(self):
        self.fail()

    def test_add_element_does_not_add_sub_elements(self):

        class TestPage(Page):
            _name = "test_page"
            def _load_elements(self):
                self.add_element("some_element", Element(self.driver, "some/path"))

        class TestApplication(Application):
            def _load_elements(self):
                self.add_page(TestPage(self.driver, self.base_url + '/'))

        app = TestApplication(None, "")
        with self.assertRaises(ElementNotFoundError):
            app.get_element("some_element")
