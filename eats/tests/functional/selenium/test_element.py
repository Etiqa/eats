import unittest
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Remote, Firefox, Chrome, ActionChains
from testserver_selenium import SimpleWebServerProcessSelenium as SimpleServer
from selenium.common.exceptions import NoSuchElementException
from eats.element import Element
from eats.common.exceptions import SearchByElementException
from selenium.webdriver.common.keys import Keys

__author__ = 'vtusan'

"""
Tests for element module using Firefox and Chrome drivers selenium.
"""


class SeleniumElementTestBase(object):
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

    def test_check_if_pytractor_driver(self):
        self.assertIsInstance(self.driver, Remote)

    def test_find_element_by_exception_not_supported(self):
        el = Element(self.driver, 'greeting', 'notsupported')
        with self.assertRaises(SearchByElementException):
            el.web_element()

    def test_find_element_by_xpath_exception_not_found(self):
        el = Element(self.driver, "//[@id='xpath_not_found']", 'xpath')
        with self.assertRaises(NoSuchElementException):
            el.web_element()

    def test_find_element_by_default_type(self):
        el = Element(self.driver, "//[@id='xpath_not_found']")
        self.assertEqual(el.search_by, 'xpath')

    def test_find_element_by_xpath(self):
        el = Element(self.driver, "//div[@id='checkboxes']", 'xpath')
        self.assertIsInstance(el.web_element, WebElement)

    def test_find_element_by_binding_exception(self):
        el = Element(self.driver, 'greeting', 'binding')
        with self.assertRaises(SearchByElementException):
            el.web_element()

    def test_find_element_by_model_exception(self):
        el = Element(self.driver, 'username', 'model')
        with self.assertRaises(SearchByElementException):
            el.web_element()

    def test_if_exists_element(self):
        el = Element(self.driver, "//div[@id='checkboxes']", 'xpath')
        self.assertTrue(el.is_present())

    def test_if_not_exists_element(self):
        el = Element(self.driver, "//div[@id='NOTEXIST']", 'xpath')
        self.assertFalse(el.is_present())

    def test_get_tag_name_element(self):
        el = Element(self.driver, "//div[@id='checkboxes']", 'xpath')
        self.assertEqual(el.tag_name, u'div')

    def test_get_text_name_element(self):
        el = Element(self.driver, "//div[@id='checkboxes']", 'xpath')
        self.assertEqual(el.text, u'Checkboxes\nShow? Shown!! W X Y Z')

    def test_get_element_type_element(self):
        el = Element(self.driver, "//div[@id='checkboxes']", 'xpath')
        self.assertEqual(el.element_type, 'element')

    def test_get_css_property_element(self):
        el = Element(self.driver, "//div[@id='checkboxes']", 'xpath')
        self.assertEqual(el.value_of_css_property('text-decoration'), u'none')

    def test_move_to_next_element_from_element(self):
        el = Element(self.driver, "//input[@ng-true-value='w']", 'xpath')
        el.move_to_element()
        self.assertFalse(el.is_selected())

    def test_selected_element(self):
        el = Element(self.driver, "//input[@ng-true-value='w']", 'xpath')
        el.click()
        self.assertTrue(el.is_selected())

    def test_is_enabled_element(self):
        el = Element(self.driver, "//button[@id='exacttext']", 'xpath')
        self.assertTrue(el.is_enabled())

    def test_is_disabled_element(self):
        el = Element(self.driver, "//button[@id='exacttext']", 'xpath')
        self.assertFalse(el.is_disabled())

    def test_is_displayed_for_displayed_element(self):
        el = Element(self.driver, "//button[@id='exacttext']", 'xpath')
        self.assertTrue(el.is_displayed())

    def test_is_displayed_for_not_displayed_element(self):
        el = Element(self.driver, "//button[@id='hiddenbutton']", 'xpath')
        self.assertFalse(el.is_displayed())

    def test_click_element(self):
        el = Element(self.driver, "//input[@ng-true-value='w']", 'xpath')
        el.click()
        el2 = Element(self.driver, "//span[@id='letterlist']", 'xpath')
        self.assertEqual(el2.text, u'w')

    def test_double_click_element(self):
        el = Element(self.driver, "//input[@ng-model='username']", 'xpath')
        self.assertIsNone(el.double_click())

    def test_get_attribute_element(self):
        el = Element(self.driver, "//div[@id='checkboxes']")
        self.assertEqual(el.get_attribute('class'), u'ng-scope')


class FirefoxWebDriverTest(SeleniumElementTestBase, unittest.TestCase):
    driver_class = Firefox


class ChromeWebDriverTest(SeleniumElementTestBase, unittest.TestCase):
    driver_class = Chrome
