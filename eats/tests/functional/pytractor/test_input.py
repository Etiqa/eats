from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.element.input import Input

__author__ = 'vtusan'

"""
Tests for input module using Firefox and Chrome drivers pytractor.
"""


class PytractorInputTestCase(PytractorTestBaseSetup):

    def test_get_element_type_element(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Input(self.driver, "appCtrl.textField", "model")
        self.assertEqual(input_el.element_type, 'input_type')

    def test_get_value(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Input(self.driver, "appCtrl.textFieldFull", "model")
        self.assertEqual(input_el.get_value(), u'Hello World')

    def test_set_value(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Input(self.driver, "appCtrl.textField", "model")
        input_el.set_value(u'Test')
        self.assertEqual(input_el.get_value(), u'Test')

    def test_send_keys(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Input(self.driver, "appCtrl.textFieldFull", "model")
        input_el.send_keys(" Test")
        self.assertEqual(input_el.get_value(), u'Hello World Test')

    def test_placeholder(self):
        self.driver.get(self.base_url + '/index.html#/form')
        input_el = Input(self.driver, "appCtrl.placeHolder", "model")
        self.assertEqual(input_el.get_placeholder(), u'Last name')

    def test_clear(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Input(self.driver, "appCtrl.textFieldFull", "model")
        input_el.clear()
        self.assertEqual(input_el.get_value(), u'')
