import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from pytractor.webdriver import WebDriverMixin

from eats.tests.common.base_test_setup import PytractorTestBaseSetup
from eats.element import Element
from eats.page import Page
from eats.common.exceptions import SearchByElementError, ElementRedefinedError


class PytractorCompoundElementTestCase(PytractorTestBaseSetup):

    def setUp(self):
        super(PytractorCompoundElementTestCase, self).setUp()

        class TestCompoundElement(Element):
            def _load_elements(self):
                self.add_element("textValue", Element(self.driver, self.path + "//span[@id='textValue']", "xpath"))

        class TestPage(Page):
            def _load_elements(self):
                self.add_element("form", TestCompoundElement(self.driver, "//form"))

        self.page = TestPage(self.driver, self.base_url + '/index.html')
        self.el = self.page.get_element("form")

    def test_get_element_type_element(self):
        self.assertEqual(self.el.element_type, 'element')

    def test_get_subelement(self):
        self.assertIsNotNone(self.el.get_element("textValue"))

    def test_subelement_is_an_element(self):
        self.assertTrue(isinstance(self.el.get_element("textValue"), Element))

    def test_subelement_web_element(self):
        self.driver.get(self.page.url)
        self.assertIsNotNone(self.el.get_element("textValue").web_element)

    def test_sub_element_is_directly_accessible_from_page(self):
        self.assertIsNotNone(self.page.get_element("textValue"))

    def test_recursively_add_sub_elements_bug(self):
        """
        In the following hierarchy, level1 directly contains level3 and level2 elements.
        When level0 added its elements, level3 was added twice:
        - as a direct child of level1
        - and as child of level2.
        This was caused by level0._add_sub_elements() calling add_element() 
        which in turn recursively called _add_sub_elements().
        """

        class Level0(Element):
            def _load_elements(self):
                self.add_element("level1", Level1(self.driver, ""))

        class Level1(Element):
            def _load_elements(self):
                self.add_element("level2", Level2(self.driver, ""))

        class Level2(Element):
            def _load_elements(self):
                self.add_element("level3", Element(self.driver, ""))

        try:
            level0 = Level0(None, "")
            self.assertIsNotNone(level0.get_element('level3'))
        except ElementRedefinedError as e:
            self.fail(e)
