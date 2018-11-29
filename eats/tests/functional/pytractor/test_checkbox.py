from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.element.checkbox import Checkbox

__author__ = 'vtusan'

"""
Tests for input module using Firefox and Chrome drivers pytractor.
"""


class PytractorCheckboxTestCase(PytractorTestBaseSetup):

    def test_get_element_type_element(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkField", "model")
        self.assertEqual(checkbox_el.element_type, 'checkbox')

    def test_get_value_true(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkFieldTrue", "model")
        self.assertTrue(checkbox_el.get_value())

    def test_get_value_false(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkField", "model")
        self.assertFalse(checkbox_el.get_value())

    def test_set_value_false(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkFieldTrue", "model")
        checkbox_el.set_value(False)
        self.assertFalse(checkbox_el.get_value())

    def test_set_value_true(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkField", "model")
        checkbox_el.set_value(True)
        self.assertTrue(checkbox_el.get_value())

    def test_is_selected_false(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkField", "model")
        self.assertFalse(checkbox_el.is_selected())

    def test_is_selected_true(self):
        self.driver.get(self.base_url + '/index.html')
        checkbox_el = Checkbox(self.driver, "appCtrl.checkFieldTrue", "model")
        self.assertTrue(checkbox_el.is_selected())
