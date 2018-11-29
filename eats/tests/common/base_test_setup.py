import socket
import unittest
from eats.webdriver import PytractorWebDriver
from eats.tests.common import SimpleWebServerProcess as SimpleServer

def _get_local_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    local_ip_addr = s.getsockname()[0]
    s.close()
    return local_ip_addr

class PytractorTestBaseSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.process = SimpleServer()
        cls.process.run()

    def setUp(self):
        self.base_url = "http://{}:{}".format(_get_local_ip_addr(), SimpleServer.PORT)
        self.driver = self.get_driver()
        self.driver.ignore_synchronization = False

    @classmethod
    def tearDownClass(cls):
        cls.process.stop()

    def tearDown(self):
        self.driver.quit()

class FirefoxRemoteWebDriverTest(object):

    def get_driver(self):
        return PytractorWebDriver(
            test_timeout=3000,
            command_executor='http://{}:4444/wd/hub'.format(_get_local_ip_addr()),
            desired_capabilities={'browserName': 'firefox', 'version': '', 'platform': 'ANY'}
        )

class ChromeRemoteWebDriverTest(object):

    def get_driver(self):
        return PytractorWebDriver(
            test_timeout=3000,
            command_executor='http://{}:4444/wd/hub'.format(_get_local_ip_addr()),
            desired_capabilities={'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
        )