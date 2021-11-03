import unittest
from user import add_user

class TestUser(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(add_user('bonjour'), True)
        self.assertEqual(add_user('Robin'), True)
        self.assertEqual(add_user(42), False)