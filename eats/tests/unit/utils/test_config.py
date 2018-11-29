import unittest
from hamcrest import *
from eats.utils.config import Configurator


class ConfiguratorTest(unittest.TestCase):

    def setUp(self):
        context = FakeContext()
        self.context = context

    def test_setup(self):
        context = self.context
        Configurator.setup(self.context)
        assert_that(context.eats, is_(instance_of(Configurator)))


class FakeContext(object):
    pass