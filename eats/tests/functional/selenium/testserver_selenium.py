import logging

from eats.tests.common import SimpleWebServerProcess

"""
This is the web server that serves the angular app that we use for testing.
It is started by setup_package() in __init__.py
"""

logger = logging.getLogger(__name__)


class SimpleWebServerProcessSelenium(SimpleWebServerProcess):
    """
    A simple webserver for serving pages for testing.
    """
    HOST = 'localhost'
    PORT = 9999
    APP_DIR = 'selenium/testapp_selenium'
    _pid = None
