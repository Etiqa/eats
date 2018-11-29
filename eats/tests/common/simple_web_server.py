import six
if six.PY2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen, HTTPError, URLError
import logging
import os
import signal
import http.server
import socketserver
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)


class SimpleServerHandler(http.server.SimpleHTTPRequestHandler):
    """
    The handler for the web server. It has the same functionality as the
    server for protractor's test app.
    """

    def send_text_response(self, text):
        self.send_response(200)
        self.send_header("Content-type", 'text/plain')
        self.send_header("Content-Length", len(text))
        self.end_headers()
        self.wfile.write(text.encode('utf-8'))

    def log_message(self, msg_format, *args):
        """Use python logging to avoid lots of output during testing."""
        logger.info("TESTSERVER: %s - - [%s] %s\n" %
                    (self.client_address[0],
                     self.log_date_time_string(),
                     msg_format % args))


class SimpleWebServerProcess(object):
    """
    A simple webserver for serving pages for testing.
    """
    HOST = '0.0.0.0'
    PORT = 9999
    APP_DIR = 'ng-app/app/'
    _pid = None

    def get_module_path(self):
        return os.path.dirname(__file__)

    def get_handler(self):
        return SimpleServerHandler

    def get_application_path(self):
        return os.path.join(self.get_module_path(), self.APP_DIR)

    def run(self):
        self._pid = os.fork()
        if self._pid == 0:
            self.start_server()
            exit() #ensure the child process exits instead of running parent's program
        else:
            logger.debug('Started webserver child as pid {} on'
                         ' port {}'.format(self._pid, self.PORT))
            # wait 5 seconds for server to start
            connected = False
            elapsed = 0
            while (not connected) and (elapsed < 5):
                try:
                    urlopen('http://localhost:{}/'.format(self.PORT), timeout=5)
                    connected = True
                except HTTPError:
                    connected = True
                except URLError:
                    time.sleep(0.1)
                    elapsed += 0.1
            if not connected:
                self.stop()
                raise Exception('webserver: fork failed')

    def start_server(self):
        server_path = self.get_application_path()
        logger.debug('Starting webserver for path {} on'
                     ' port {}'.format(server_path, self.PORT))
        os.chdir(server_path)
        handler = self.get_handler()
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer((self.HOST, self.PORT), handler)
        httpd.serve_forever()

    def stop(self):
        if self._pid != 0:
            logger.debug('Sending SIGTERM to webserver child with'
                         ' pid {}'.format(self._pid))
            os.kill(self._pid, signal.SIGTERM)
            os.waitpid(self._pid, 0)
