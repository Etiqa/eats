import unittest
import time
from selenium.webdriver import Firefox, Chrome
from testserver_selenium import SimpleWebServerProcessSelenium as SimpleServer
from eats.element.input import Input

__author__ = 'vtusan'

"""
Tests for input module using Firefox and Chrome drivers selenium.
"""


class SeleniumInputTestBase(object):
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
        input_el = Input(self.driver, "//input[@ng-model='username']")
        self.assertEqual(input_el.element_type, 'input_type')

    def test_get_value(self):
        input_el = Input(self.driver, "//input[@ng-model='username']")
        self.assertEqual(input_el.get_value(), u'Anon')

    def test_set_value(self):
        input_el = Input(self.driver, "//input[@ng-model='username']")
        input_el.set_value(u'Test')
        self.assertEqual(input_el.get_value(), u'Test')

    def test_send_keys(self):
        input_el = Input(self.driver, "//input[@ng-model='username']")
        input_el.send_keys("Test")
        self.assertEqual(input_el.get_value(), u'AnonTest')

    def test_placeholder(self):
        input_el = Input(self.driver, "//input[@ng-model='username']")
        self.assertEqual(input_el.get_placeholder(), u'Username')

    def test_clear(self):
        input_el = Input(self.driver, "//input[@ng-model='username']")
        input_el.clear()
        self.assertEqual(input_el.get_value(), u'')

class FirefoxWebDriverTest(SeleniumInputTestBase, unittest.TestCase):
    driver_class = Firefox


class ChromeWebDriverTest(SeleniumInputTestBase, unittest.TestCase):
    driver_class = Chrome
