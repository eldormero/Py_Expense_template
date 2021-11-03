import unittest
from status import get_status

class TestStatus(unittest.TestCase):

    def test_get_status(self):
        self.assertEqual(get_status(), True)

