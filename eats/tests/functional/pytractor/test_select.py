from pytractor.webdriver import WebDriverMixin

from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.element import Select

__author__ = 'vtusan'

"""
Tests for input module using Firefox and Chrome drivers pytractor.
"""


class PytractorSelectTestCase(PytractorTestBaseSetup):

    def test_get_element_type_element(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        self.assertEqual('select_type', input_el.element_type)

    def test_get_value(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        self.assertEqual(u'1', input_el.get_value())

    def test_set_value(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        input_el.set_value(u'2')
        self.assertEqual(u'2', input_el.get_value())

    def test_get_selected_option_label(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        self.assertEqual(u'option 1', input_el.get_selected_option_label())

    def test_set_value_by_label(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        input_el.set_value_by_label('option 2')
        self.assertEqual(u'2', input_el.get_value())

    def test_get_values(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        self.assertItemsEqual(['1', '2', '3', '4'], input_el.get_options_values())

    def test_get_labels(self):
        self.driver.get(self.base_url + '/index.html')
        input_el = Select(self.driver, "appCtrl.selectField", "model")
        self.assertItemsEqual(['option 1', 'option 2', 'option 3', 'option 4'], input_el.get_options_labels())
