import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from pydactyl import PterodactylClient


class ServersTests(unittest.TestCase):

    def setUp(self):
        self.client = PterodactylClient(url='dummy', api_key='dummy')


if __name__ == '__main__':
    unittest.main()
