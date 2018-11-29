from eats.application import Application
from eats.tests.common import SimpleWebServerProcess as SimpleServer

from pages import Index


class TestApplication(Application):
    def _load_elements(self):
        self.add_page(Index(self.driver, self.base_url + "/index.html"))

    def start(self):
        self.process = SimpleServer()
        self.process.run()

    def stop(self):
        self.process.stop()
