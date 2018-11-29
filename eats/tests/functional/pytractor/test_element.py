import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from pytractor.webdriver import WebDriverMixin

from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.element import Element
from eats.common.exceptions import SearchByElementError

"""
Tests for element module using Firefox and Chrome drivers pytractor.
"""


class PytractorElementTestCase(PytractorTestBaseSetup):

    def test_check_if_pytractor_driver(self):
        self.assertIsInstance(self.driver, WebDriverMixin)

    def test_get_element_type_element(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='checkValue']")
        self.assertEqual(el.element_type, 'element')

    def test_find_element_by_exception_not_supported(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, 'greeting', 'notsupported')
        with self.assertRaises(SearchByElementError):
            el.web_element()

    def test_find_element_by_defualt_type(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='radioValue']")
        self.assertEqual(el.search_by, 'xpath')

    def test_find_element_by_xpath_exception_not_found(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='xpath_not_found']", 'xpath')
        with self.assertRaises(NoSuchElementException):
            el.web_element()

    def test_find_element_by_exact_binding_exception_not_found(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, 'biding_not_found', 'exact_binding')
        with self.assertRaises(NoSuchElementException):
            el.web_element()

    @unittest.expectedFailure
    def test_find_element_by_binding_exception_not_found(self):
        self.fail()

    def test_find_element_by_model_exception_not_found(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, 'model_not_found', 'model')
        with self.assertRaises(NoSuchElementException):
            el.web_element()

    def test_find_element_by_default(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='checkValue']")
        self.assertIsInstance(el.web_element, WebElement)
        self.assertEqual(el.search_by, 'xpath')

    def test_find_element_by_xpath(self):
        self.driver.get(self.base_url + '/index.html#/form')
        el = Element(self.driver, "//span[@id='checkValue']", 'xpath')
        self.assertIsInstance(el.web_element, WebElement)

    def test_find_element_by_exact_binding(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, 'appCtrl.checkField', 'exact_binding')
        self.assertIsInstance(el.web_element, WebElement)

    @unittest.expectedFailure
    def test_find_element_by_binding(self):
        self.fail()

    def test_find_element_by_model(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, 'appCtrl.checkField', 'model')
        self.assertIsInstance(el.web_element, WebElement)

    def test_exists_element(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='checkValue']", 'xpath')
        self.assertTrue(el.is_present())

    def test_if_not_exists_element(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//div[@id='NOTEXIST']", 'xpath')
        self.assertFalse(el.is_present())

    def test_get_tag_name(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='checkValue']", 'xpath')
        self.assertEqual(el.tag_name, u'span')

    def test_get_attribute_element(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "appCtrl.checkField", "model")
        self.assertEqual(el.get_attribute('type'), u'checkbox')

    def test_get_element_text(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "appCtrl.textFieldFull", "exact_binding")
        self.assertEqual(el.text, u'Hello World')

    def test_get_css_property_element(self):
        self.driver.get(self.base_url + '/index.html#/form')
        el = Element(self.driver, "//span[@id='textValueFull']", 'xpath')
        self.assertEqual(el.value_of_css_property('color'), u'rgba(255, 0, 0, 1)')

    def test_move_to_element(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//span[@id='textValueFull']", 'xpath')
        self.assertEqual(el.value_of_css_property('color'), u'rgba(255, 0, 0, 1)')
        el.move_to_element()
        self.assertEqual(el.value_of_css_property('color'), u'rgba(0, 0, 0, 1)')

    def test_is_selected(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Element(self.driver, "appCtrl.checkFieldTrue", "model")
        self.assertTrue(checkbox_el.is_selected())

    def test_click_element(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Element(self.driver, "appCtrl.checkField", "model")
        checkbox_el.click()
        self.assertTrue(checkbox_el.is_selected())

    @unittest.skip("test_double_click skipping")
    def test_double_click(self):
        self.driver.get(self.base_url + '/index.html')
        assert False

    @unittest.skip("test_is_displayed skipping")
    def test_is_displayed(self):
        self.driver.get(self.base_url + '/index.html')
        assert False

    def test_if_element_is_not_present_it_is_not_displayed(self):
        self.driver.get(self.base_url + '/index.html')
        el = Element(self.driver, "//div[@id='NOTEXIST']", 'xpath')
        self.assertFalse(el.is_present())
        self.assertFalse(el.is_displayed())

    @unittest.expectedFailure
    def test_ambiguous_element_query_raises_exception(self):
        self.fail()

    def test_fading_in_element_is_not_displayed_if_opacity_is_zero(self):
        self.driver.ignore_synchronization = True
        self.driver.get(self.base_url + '/test_fadein.html')
        Element(self.driver, "//button[@id='button']", "xpath").click()
        el = Element(self.driver, "//div[@id='test']/p", "xpath")
        self.assertFalse(el.is_displayed())

    def test_fading_in_element_is_displayed_after_some_delay(self):
        self.driver.ignore_synchronization = True
        self.driver.get(self.base_url + '/test_fadein.html')
        Element(self.driver, "//button[@id='button']", "xpath").click()
        el = Element(self.driver, "//div[@id='test']/p", "xpath", 2500)
        self.assertTrue(el.is_displayed())
