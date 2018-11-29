from eats.page import Page
from eats.element import Element, Input, Checkbox


class Index(Page):
    _name = "index"

    def _load_elements(self):
        self.add_element('title', Element(self.driver, "//h1", "xpath"))
        self.add_element('textField', Input(self.driver, "appCtrl.textField", "model"))
        self.add_element('textFieldFull', Input(self.driver, "appCtrl.textFieldFull", "model"))
        self.add_element('checkboxFalse', Checkbox(self.driver, "appCtrl.checkField", 'model'))
        self.add_element('checkboxTrue', Checkbox(self.driver, "appCtrl.checkFieldTrue", 'model'))

        self.add_element('ELEMENT_NOT_ON_PAGE', Element(self.driver, "//h2", 'xpath'))

    def goto(self):
        self.driver.get(self.url)
