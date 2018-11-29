import unittest
import xmlrunner
from eats.tests.common.base_test_setup import PytractorTestBaseSetup, ChromeRemoteWebDriverTest, FirefoxRemoteWebDriverTest
import six
if six.PY2:
    py = "python27"
else:
    py = "python36"

__author__ = 'vtusan'

test_modules = [
    # 'eats.tests.functional.pytractor.test_compound_element',
    # 'eats.tests.functional.pytractor.test_element',
    # 'eats.tests.functional.pytractor.test_input',
    # 'eats.tests.functional.pytractor.test_checkbox',
    # 'eats.tests.functional.pytractor.test_select',
    # 'eats.tests.functional.pytractor.test_page',
    # 'eats.tests.functional.pytractor.test_application',
    # 'eats.tests.unit.test_utils',
    'eats.tests.unit.test_users',
    'eats.tests.unit.test_workspace',
    # 'eats.tests.functional.selenium.test_element',
    # 'eats.tests.functional.selenium.test_page',
    # 'eats.tests.functional.selenium.test_input',
    # 'eats.tests.functional.selenium.test_checkbox',
    # 'eats.tests.functional.selenium.test_application',
    'eats.tests.unit.utils.test_sitemap'

]


def run_test_suite(test_modules_path):

    test_suite = unittest.TestSuite()
    for test_module in test_modules_path:
        # load all the test cases from the defined modules.
        m = __import__(test_module, fromlist=[''])
        test_cases = [member for member in map(lambda name: getattr(m, name), dir(m))
                      if isinstance(member, type) and issubclass(member, unittest.TestCase)]
        for test_case in test_cases:
            if issubclass(test_case, PytractorTestBaseSetup):
                chrome_test_case = type(test_case.__name__, (ChromeRemoteWebDriverTest, test_case), {})
                firefox_test_case = type(test_case.__name__, (FirefoxRemoteWebDriverTest, test_case), {})
                test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(chrome_test_case))
                test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(firefox_test_case))
            else:
                test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test_case))
    with open('test_reports/' + py + 'results.xml', 'wb') as output:
        testRunner = xmlrunner.XMLTestRunner(output=output)
        testRunner.run(test_suite)


run_test_suite(test_modules)


"""
these tests use Selenium Grid and remote webdrivers. In order for this to work, follow these steps:
- (start Selenium Grid Hub on local machine)
  java -jar selenium-server-standalone-2.53.0.jar -role hub
- (start Selenium Grid Node on remote machine)
  java -jar selenium-server-standalone-2.53.0.jar -role node -hub http://HUB_IP_ADDRESS:4444/grid/register
- (run the test suite on the Hub)
  python -m eats.tests.run_test_suite
"""
