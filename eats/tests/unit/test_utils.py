import unittest
from eats.common.utils import get_root_url


class TestUtilsMethods(unittest.TestCase):

    def test_get_root_url_local_url(self):
        self.assertEqual(get_root_url('http://localhost/'), 'http://localhost/')

    def test_get_root_url_local_url_with_port(self):
        self.assertEqual(get_root_url('http://localhost:9998/'), 'http://localhost:9998/')

    def test_get_root_url_local_url_with_path(self):
        self.assertEqual(get_root_url('http://localhost/favicon.ico'), 'http://localhost/')

    def test_get_root_url_local_url_with_fragment(self):
        self.assertEqual(get_root_url('http://localhost/#/form'), 'http://localhost/')

    def test_get_root_url_local_url_with_fragment_and_port(self):
        self.assertEqual(get_root_url('http://localhost:9998/#/favicon.ico'), 'http://localhost:9998/')

    def test_get_root_url_local_url_with_query(self):
        self.assertEqual(get_root_url('http://localhost/?favicon.ico'), 'http://localhost/')

    def test_get_root_url_local_url_with_query_and_port(self):
        self.assertEqual(get_root_url('http://localhost:9998/?favicon.ico'), 'http://localhost:9998/')

    def test_get_root_url_remote_url(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com/'), 'http://www.hoverstate.com/')

    def test_get_root_url_remote_url_with_port(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com:8080/'), 'http://www.hoverstate.com:8080/')

    def test_get_root_url_remote_url_with_path(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com/favicon.ico'), 'http://www.hoverstate.com/')

    def test_get_root_url_remote_url_with_fragment(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com/#/form'), 'http://www.hoverstate.com/')

    def test_get_root_url_remote_url_with_fragment_and_port(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com:8080/#/favicon.ico'), 'http://www.hoverstate.com:8080/')

    def test_get_root_url_remote_url_with_query(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com/?favicon.ico'), 'http://www.hoverstate.com/')

    def test_get_root_url_remote_url_with_query_and_port(self):
        self.assertEqual(get_root_url('http://www.hoverstate.com:8080/?favicon.ico'), 'http://www.hoverstate.com:8080/')

if __name__ == '__main__':
    unittest.main()