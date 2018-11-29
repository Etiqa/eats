import unittest
import time

from selenium.webdriver import Firefox, Chrome
from testserver_selenium import SimpleWebServerProcessSelenium as SimpleServer
from eats.element.checkbox import Checkbox

__author__ = 'vtusan'

"""
Tests for checkbox module using Firefox and Chrome drivers selenium.
"""


class SeleniumCheckboxTestBase(object):
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

    def test_get_element_type_element(self):
        self.driver.get(self.base_url + 'index.html')
        checkbox_el = Checkbox(self.driver, "//input[@ng-model='show']")
        self.assertEqual(checkbox_el.element_type, 'checkbox')

    def test_get_value(self):
        self.driver.get(self.base_url + 'index.html')
        checkbox_el = Checkbox(self.driver, "//input[@ng-model='show']")
        self.assertTrue(checkbox_el.get_value())

    def test_set_value_false(self):
        self.driver.get(self.base_url + 'index.html')
        checkbox_el = Checkbox(self.driver, "//input[@ng-model='show']")
        checkbox_el.set_value(False)
        self.assertFalse(checkbox_el.get_value())

    def test_set_value_true(self):
        self.driver.get(self.base_url + 'index.html')
        checkbox_el = Checkbox(self.driver, "//input[@ng-true-value='w']")
        checkbox_el.set_value(True)
        self.assertTrue(checkbox_el.get_value())

    def test_is_selected_false(self):
        self.driver.get(self.base_url + 'index.html')
        checkbox_el = Checkbox(self.driver, "//input[@ng-true-value='w']")
        self.assertFalse(checkbox_el.is_selected())

    def test_is_selected_true(self):
        self.driver.get(self.base_url + 'index.html')
        checkbox_el = Checkbox(self.driver, "//input[@ng-model='show']")
        self.assertTrue(checkbox_el.is_selected())


class FirefoxWebDriverTest(SeleniumCheckboxTestBase, unittest.TestCase):
    driver_class = Firefox


class ChromeWebDriverTest(SeleniumCheckboxTestBase, unittest.TestCase):
    driver_class = Chrome
